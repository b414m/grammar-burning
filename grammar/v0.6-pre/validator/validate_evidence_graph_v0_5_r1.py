#!/usr/bin/env python3
import argparse, hashlib, json, re
from pathlib import Path

HEX64 = re.compile(r"^[0-9a-f]{64}$")
ENTITY_GROUPS = {
    "artifacts":"artifact", "tests":"test", "executions":"execution", "claims":"claim",
    "capabilities":"capability", "contracts":"contract", "evidence":"evidence",
    "requirements":"requirement", "transitions":"transition", "invariants":"invariant",
    "environments":"environment"
}

def sha256_file(p: Path):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()

def safe_materialized_path(root: Path, rel: str):
    if not isinstance(rel,str) or not rel or Path(rel).is_absolute(): return None
    if '\\' in rel: return None
    target=(root/rel).resolve()
    try: target.relative_to(root.resolve())
    except ValueError: return None
    return target

def materialized_entity(entity, package_root, artifacts, evidence, errors, label):
    eid=entity.get('id')
    if eid in artifacts:
        a=artifacts[eid]; rel=a.get('path'); declared=a.get('sha256')
    elif eid in evidence:
        a=evidence[eid]; rel=a.get('path'); declared=a.get('sha256')
    else:
        errors.append(f"{label}: result entity {eid!r} is neither artifact nor evidence")
        return False
    target=safe_materialized_path(package_root, rel)
    if target is None:
        errors.append(f"{label}: unsafe/non-canonical result path {rel!r}"); return False
    if not target.is_file():
        errors.append(f"{label}: materialized result missing at {rel!r}"); return False
    if not HEX64.match(str(declared or '')):
        errors.append(f"{label}: result {eid} missing/invalid sha256"); return False
    actual=sha256_file(target)
    if actual != declared:
        errors.append(f"{label}: result {eid} sha256 mismatch"); return False
    return True

def success_is_valid(e, model, errors):
    if e.get('status') != 'PASSED': return True
    sem=e.get('success_semantics')
    if not isinstance(sem,dict):
        errors.append(f"execution {e['id']}: PASSED requires typed success_semantics object")
        return False
    kind=sem.get('kind'); allowed=model.get('success_semantics',{}).get('allowed_kinds',{})
    if kind not in allowed:
        errors.append(f"execution {e['id']}: unsupported success_semantics kind {kind!r}")
        return False
    missing=[f for f in allowed[kind].get('required_fields',[]) if f not in sem]
    if missing:
        errors.append(f"execution {e['id']}: success_semantics missing {missing}")
        return False
    ok=False
    if kind=='exit_code':
        observed=sem.get('observed'); accepted=sem.get('accepted_codes')
        ok=isinstance(accepted,list) and observed in accepted and observed==e.get('exit_code')
    elif kind=='assertion_summary':
        ok=isinstance(sem.get('passed'),int) and isinstance(sem.get('failed'),int) and sem['passed']>=0 and sem['failed']==0
    elif kind=='predicate':
        ok=sem.get('observed') == sem.get('expected') and bool(sem.get('predicate_id'))
    if not ok:
        errors.append(f"execution {e['id']}: typed success predicate is not satisfied")
    return ok

def validate(doc, contract, grammar, model, package_root):
    errors=[]; entities={}; entity_kind={}
    forbidden=set(model.get('normative_field_policy',{}).get('forbidden_legacy_fields',[]))
    for e in doc.get('executions',[]):
        for key in ('witnesses','witness_bindings'):
            if key in e or key in forbidden and key in e:
                errors.append(f"execution {e.get('id')}: forbidden legacy field {key}")
    for c in doc.get('claims',[]):
        if 'required_witnesses' in c:
            errors.append(f"claim {c.get('id')}: forbidden legacy field required_witnesses")
    if 'reachability_witnesses' in doc:
        errors.append('graph: forbidden legacy field reachability_witnesses')

    for group,kind in ENTITY_GROUPS.items():
        for e in doc.get(group,[]):
            eid=e.get('id')
            if not eid: errors.append(f"{group}: entity missing id"); continue
            if eid in entities: errors.append(f"duplicate id: {eid}")
            entities[eid]=e; entity_kind[eid]=kind

    artifacts={a['id']:a for a in doc.get('artifacts',[]) if a.get('id')}
    evidence={a['id']:a for a in doc.get('evidence',[]) if a.get('id')}
    tests={a['id']:a for a in doc.get('tests',[]) if a.get('id')}
    executions={e['id']:e for e in doc.get('executions',[]) if e.get('id')}
    capabilities={e['id']:e for e in doc.get('capabilities',[]) if e.get('id')}
    requirements={e['id']:e for e in doc.get('requirements',[]) if e.get('id')}
    claims={e['id']:e for e in doc.get('claims',[]) if e.get('id')}
    relations={r.get('id'):r for r in doc.get('relations',[]) if r.get('id')}

    seen_paths={}
    for aid,a in artifacts.items():
        rel=a.get('path'); declared=a.get('sha256')
        target=safe_materialized_path(package_root, rel)
        if target is None:
            errors.append(f"artifact {aid}: unsafe/non-canonical relative path {rel!r}"); continue
        if rel in seen_paths and seen_paths[rel] != aid:
            errors.append(f"artifact {aid}: duplicate package path projection {rel!r}")
        seen_paths[rel]=aid
        if not target.is_file():
            errors.append(f"artifact {aid}: materialized file missing at {rel!r}"); continue
        if not HEX64.match(str(declared or '')):
            errors.append(f"artifact {aid}: invalid/missing sha256")
        elif sha256_file(target) != declared:
            errors.append(f"artifact {aid}: materialized sha256 mismatch")

    for eid,e in evidence.items():
        if e.get('path') is None: continue
        materialized_entity(e, package_root, artifacts, evidence, errors, f"evidence {eid}")

    relation_specs={x['type']:x for x in model.get('relation_types',[])}
    for r in doc.get('relations',[]):
        rid=r.get('id'); typ=r.get('type'); spec=relation_specs.get(typ)
        if not spec:
            errors.append(f"relation {rid}: untyped/unknown relation {typ!r}"); continue
        for side in ('from','to'):
            if r.get(side) not in entities: errors.append(f"relation {rid}: unresolved {side}={r.get(side)!r}")
        if r.get('from') in entity_kind and entity_kind[r['from']] not in spec.get('from',[]):
            errors.append(f"relation {rid}: invalid from-kind {entity_kind[r['from']]} for {typ}")
        if r.get('to') in entity_kind and entity_kind[r['to']] not in spec.get('to',[]):
            errors.append(f"relation {rid}: invalid to-kind {entity_kind[r['to']]} for {typ}")
        if typ=='DERIVED_FROM' and r.get('from') in entities and r.get('to') in entities:
            child,source=entities[r['from']],entities[r['to']]
            co,so=child.get('created_order'),source.get('created_order')
            if co is not None and so is not None and so >= co:
                errors.append(f"relation {rid}: causal source order {so} must be < derived order {co}")

    rel_tuples={(r.get('type'),r.get('from'),r.get('to')) for r in doc.get('relations',[])}
    produces_by_exec={eid:set() for eid in executions}; executes_by_exec={eid:set() for eid in executions}; supports_to_claim={cid:set() for cid in claims}
    for typ,frm,to in rel_tuples:
        if typ=='PRODUCES' and frm in produces_by_exec: produces_by_exec[frm].add(to)
        if typ=='EXECUTES' and frm in executes_by_exec: executes_by_exec[frm].add(to)
        if typ=='SUPPORTS' and to in supports_to_claim and frm in executions: supports_to_claim[to].add(frm)

    for e in executions.values():
        success_is_valid(e,model,errors)
        for target in e.get('sut',[]):
            aid=target.get('artifact_id'); claimed=target.get('sha256'); art=artifacts.get(aid)
            if not art: errors.append(f"execution {e['id']}: unknown SUT artifact {aid!r}"); continue
            if not HEX64.match(str(claimed or '')): errors.append(f"execution {e['id']}: invalid/missing SUT sha256 for {aid}")
            elif claimed != art.get('sha256'): errors.append(f"execution {e['id']}: stale/wrong SUT hash for {aid}")

    def test_is_grounded(test_id, label):
        t=tests.get(test_id)
        if not t: errors.append(f"{label}: test {test_id!r} missing"); return False
        sources=t.get('source_artifact_ids') or ([t.get('source_artifact_id')] if t.get('source_artifact_id') else [])
        if not sources or any(source not in artifacts for source in sources):
            errors.append(f"{label}: test {test_id} lacks materialized source_artifact_id(s)"); return False
        for source in sources:
            art=artifacts[source]
            target=safe_materialized_path(package_root, art.get('path'))
            if target is None or not target.is_file() or sha256_file(target)!=art.get('sha256'):
                errors.append(f"{label}: test {test_id} source artifact {source} is not materialized with matching identity"); return False
        return True

    def evidence_binding_valid(exec_id, binding, subject_required, label):
        e=executions.get(exec_id)
        if not e: errors.append(f"{label}: missing execution {exec_id}"); return False
        kind=binding.get('kind'); test_id=binding.get('test_id'); results=binding.get('result_entity_ids'); subjects=binding.get('subject_artifact_ids')
        if not kind or not test_id or not isinstance(results,list) or not results or not isinstance(subjects,list) or not subjects:
            errors.append(f"{label}: malformed evidence_binding {binding}"); return False
        ok=True
        if ('EXECUTES',exec_id,test_id) not in rel_tuples:
            errors.append(f"{label}: evidence binding {kind} not grounded by EXECUTES {exec_id}->{test_id}"); ok=False
        if not test_is_grounded(test_id,label): ok=False
        for rid in results:
            if ('PRODUCES',exec_id,rid) not in rel_tuples:
                errors.append(f"{label}: evidence binding {kind} result {rid} not grounded by PRODUCES"); ok=False
            ent=artifacts.get(rid) or evidence.get(rid)
            if not ent or not materialized_entity(ent, package_root, artifacts, evidence, errors, label): ok=False
        sut_ids={x.get('artifact_id') for x in e.get('sut',[])}
        for aid in subjects:
            if aid not in artifacts:
                errors.append(f"{label}: evidence binding {kind} unknown subject artifact {aid}"); ok=False
            elif aid not in sut_ids:
                errors.append(f"{label}: evidence binding {kind} subject {aid} absent from exact SUT"); ok=False
        if subject_required and set(subject_required) != set(subjects):
            errors.append(f"{label}: evidence binding {kind} subject set {subjects} != claim subject set {subject_required}"); ok=False
        return ok

    def check_verified_claim(c, extra_required=()):
        if c.get('state')!='VERIFIED': return
        cid=c['id']; support=set(c.get('supported_by',[])); edge_support=supports_to_claim.get(cid,set())
        if not support: errors.append(f"claim {cid}: VERIFIED without supporting execution")
        if support != edge_support:
            errors.append(f"claim {cid}: supported_by {sorted(support)} != typed SUPPORTS edges {sorted(edge_support)}")
        subjects=c.get('subject_artifact_ids')
        if not isinstance(subjects,list) or not subjects:
            errors.append(f"claim {cid}: VERIFIED requires subject_artifact_ids"); subjects=[]
        for aid in subjects:
            if aid not in artifacts: errors.append(f"claim {cid}: unknown subject artifact {aid}")
        required=set(c.get('required_evidence_kinds',[])) | set(extra_required)
        policy=c.get('aggregation_policy','single_execution')
        if policy!='single_execution':
            errors.append(f"claim {cid}: unsupported aggregation_policy {policy!r}; v0.5-pre only authorizes single_execution")
        candidates=[]
        for eid in support:
            e=executions.get(eid)
            if not e: errors.append(f"claim {cid}: support execution {eid!r} not found"); continue
            if e.get('status')!='PASSED': errors.append(f"claim {cid}: execution {eid} is not PASSED"); continue
            if not e.get('sut'): errors.append(f"claim {cid}: execution {eid} has no exact SUT binding")
            bindings=e.get('evidence_bindings',[])
            kinds={b.get('kind') for b in bindings if isinstance(b,dict)}
            if required.issubset(kinds):
                local_ok=True
                for kind in required:
                    bs=[b for b in bindings if b.get('kind')==kind]
                    if not bs or not any(evidence_binding_valid(eid,b,subjects,f"claim {cid}") for b in bs): local_ok=False
                if local_ok: candidates.append(eid)
        if required and not candidates:
            errors.append(f"claim {cid}: no single grounded execution satisfies required evidence kinds {sorted(required)}")

    for c in claims.values(): check_verified_claim(c)
    for inv in grammar.get('tier_a_candidates',[]):
        if not inv.get('mandatory_claim'): continue
        matches=[c for c in claims.values() if c.get('invariant_id')==inv['id'] and c.get('state')=='VERIFIED']
        if not matches:
            errors.append(f"grammar invariant {inv['id']}: missing VERIFIED invariant claim")
            continue
        for c in matches: check_verified_claim(c, inv.get('required_evidence_kinds',[]))

    req_by_obligation={}
    for req in requirements.values():
        oid=req.get('external_obligation_id')
        if oid: req_by_obligation.setdefault(oid,[]).append(req)
    contract_obligations={o['id']:o for o in contract.get('obligations',[]) if o.get('id') and o.get('required',True)}
    rw_by_cap={}
    for w in doc.get('reachability_bindings',[]):
        if w.get('capability_id'): rw_by_cap.setdefault(w['capability_id'],[]).append(w)
    target_pairs={(r.get('from'),r.get('to')) for r in doc.get('relations',[]) if r.get('type')=='TARGETS'}

    def validate_reachability(cap):
        cid=cap['id']; ws=rw_by_cap.get(cid,[])
        if not ws: errors.append(f"capability {cid}: missing production reachability binding"); return
        any_valid=False
        for w in ws:
            local=[]; entry=w.get('entrypoint_artifact_id'); exid=w.get('execution_id'); pids=w.get('path_relation_ids',[])
            entry_art=artifacts.get(entry)
            if not entry_art or entry_art.get('role')!='production_entrypoint': local.append('entrypoint is not production_entrypoint')
            ex=executions.get(exid)
            if not ex or ex.get('status')!='PASSED': local.append('execution missing/not PASSED')
            if (exid,cid) not in target_pairs: local.append('execution has no TARGETS relation to capability')
            current=entry; path_artifacts=[]
            if not pids: local.append('empty REACHES path')
            for pid in pids:
                r=relations.get(pid)
                if not r or r.get('type')!='REACHES': local.append(f"path relation {pid!r} missing/not REACHES"); break
                if r.get('from')!=current: local.append(f"path relation {pid} not contiguous from {current}"); break
                current=r.get('to')
                if entity_kind.get(current)=='artifact': path_artifacts.append(current)
            if current!=cid: local.append(f"REACHES path ends at {current!r}")
            if ex:
                sut_ids={x.get('artifact_id') for x in ex.get('sut',[])}
                for aid in [entry]+path_artifacts:
                    if aid and aid not in sut_ids: local.append(f"path artifact {aid} absent from exact SUT")
                if not produces_by_exec.get(exid): local.append('reachability execution PRODUCES no materialized result')
                else:
                    if not any(materialized_entity(artifacts.get(x) or evidence.get(x) or {'id':x}, package_root, artifacts, evidence, [], f"reachability {cid}") for x in produces_by_exec[exid]):
                        local.append('reachability execution has no valid materialized produced result')
            if not local: any_valid=True; break
        if not any_valid: errors.append(f"capability {cid}: no valid grounded reachability binding")

    for oid,o in contract_obligations.items():
        mapped=req_by_obligation.get(oid,[])
        if not mapped: errors.append(f"external obligation {oid}: no requirement binding"); continue
        if len(mapped)>1: errors.append(f"external obligation {oid}: multiple requirement bindings {[x['id'] for x in mapped]}")
        req=mapped[0]; state=o.get('required_state')
        if state=='REACHABLE':
            caps=[c for c in capabilities.values() if c.get('requirement_id')==req['id']]
            if not caps: errors.append(f"external obligation {oid}: no capability bound to requirement {req['id']}")
            for cap in caps: validate_reachability(cap)
        elif state=='VERIFIED':
            cs=[c for c in claims.values() if c.get('requirement_id')==req['id'] and c.get('state')=='VERIFIED']
            if not cs: errors.append(f"external obligation {oid}: no VERIFIED claim bound to requirement {req['id']}")
            for c in cs: check_verified_claim(c,o.get('required_evidence_kinds',[]))
        else: errors.append(f"external obligation {oid}: unsupported required_state {state!r}")

    known_obligations={o.get('id') for o in contract.get('obligations',[])}
    for oid in req_by_obligation:
        if oid not in known_obligations: errors.append(f"requirement binding references unknown external obligation {oid}")
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('evidence_graph')
    ap.add_argument('--contract',required=True)
    ap.add_argument('--grammar',required=True)
    ap.add_argument('--model',required=True)
    ap.add_argument('--package-root',required=True)
    args=ap.parse_args()
    doc=json.loads(Path(args.evidence_graph).read_text(encoding='utf-8'))
    contract=json.loads(Path(args.contract).read_text(encoding='utf-8'))
    grammar=json.loads(Path(args.grammar).read_text(encoding='utf-8'))
    model=json.loads(Path(args.model).read_text(encoding='utf-8'))
    errs=validate(doc,contract,grammar,model,Path(args.package_root))
    print(json.dumps({'valid':not errs,'error_count':len(errs),'errors':errs},indent=2,ensure_ascii=False))
    raise SystemExit(0 if not errs else 1)
if __name__=='__main__': main()
