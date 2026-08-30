#!/usr/bin/env python3
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE_PATH=HERE/'validate_evidence_graph_v0_5_r1.py'
spec=importlib.util.spec_from_file_location('v05r1',BASE_PATH)
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)

def sha256_file(p:Path):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def get_path(obj,path):
    cur=obj
    for part in path.split('.'):
        if not isinstance(cur,dict) or part not in cur: return None,False
        cur=cur[part]
    return cur,True

def pred_ok(obj,p):
    val,found=get_path(obj,p.get('path',''))
    if not found: return False
    op=p.get('op'); exp=p.get('value')
    if op=='eq': return val==exp
    if op=='gte':
        return isinstance(val,(int,float)) and not isinstance(val,bool) and isinstance(exp,(int,float)) and val>=exp
    if op=='lte':
        return isinstance(val,(int,float)) and not isinstance(val,bool) and isinstance(exp,(int,float)) and val<=exp
    if op=='contains':
        try: return exp in val
        except TypeError: return False
    return False

def safe(root,rel):
    return base.safe_materialized_path(root,rel)

def load_json_result(root,entity,errors,label):
    p=safe(root,entity.get('path'))
    if p is None or not p.is_file():
        errors.append(f'{label}: result path not materialized'); return None
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{label}: result is not parseable JSON: {exc}'); return None

def semantic_validate(doc, package_root, execution_records_path, profile):
    errors=[]
    package_root=Path(package_root).resolve()
    executions={e.get('id'):e for e in doc.get('executions',[]) if e.get('id')}
    tests={t.get('id'):t for t in doc.get('tests',[]) if t.get('id')}
    artifacts={a.get('id'):a for a in doc.get('artifacts',[]) if a.get('id')}
    evidence={e.get('id'):e for e in doc.get('evidence',[]) if e.get('id')}
    claims={c.get('id'):c for c in doc.get('claims',[]) if c.get('id')}
    rels=doc.get('relations',[])
    executes_by={}; produces_by={}; supports_by={}
    for r in rels:
        if r.get('type')=='EXECUTES': executes_by.setdefault(r.get('from'),set()).add(r.get('to'))
        if r.get('type')=='PRODUCES': produces_by.setdefault(r.get('from'),set()).add(r.get('to'))
        if r.get('type')=='SUPPORTS': supports_by.setdefault(r.get('to'),set()).add(r.get('from'))

    auth=profile.get('authority',{}).get('execution_records',{})
    expected_rel=auth.get('relative_path'); expected_sha=auth.get('sha256')
    canonical=safe(package_root,expected_rel)
    supplied=Path(execution_records_path).resolve()
    if canonical is None or supplied!=canonical:
        errors.append('authority: execution_records path is not the canonical package-root authority')
    if not supplied.is_file():
        errors.append('authority: execution_records file missing')
        records={}
    else:
        actual=sha256_file(supplied)
        if actual!=expected_sha: errors.append('authority: execution_records sha256 mismatch')
        try:
            recdoc=json.loads(supplied.read_text(encoding='utf-8'))
            records={r.get('id'):r for r in recdoc.get('records',[]) if r.get('id')}
        except Exception as exc:
            errors.append(f'authority: execution_records invalid JSON: {exc}'); records={}

    def entity_by_path_sha(pool,path,sha):
        return [eid for eid,e in pool.items() if e.get('path')==path and e.get('sha256')==sha]

    record_for_exec={}
    selector_for_test={}
    for tid,t in tests.items():
        sel=t.get('invocation_selector')
        if not isinstance(sel,dict) or sel.get('kind')!='command_arg_equals' or not isinstance(sel.get('index'),int) or 'value' not in sel:
            errors.append(f'test {tid}: missing/invalid invocation_selector')
            continue
        selector_for_test[tid]=sel

    for eid,e in executions.items():
        rid=e.get('execution_record_id')
        if not rid:
            errors.append(f'execution {eid}: missing execution_record_id'); continue
        rec=records.get(rid)
        if not rec:
            errors.append(f'execution {eid}: unknown authoritative execution_record_id {rid!r}'); continue
        record_for_exec[eid]=rec
        if e.get('command')!=rec.get('command'): errors.append(f'execution {eid}: command contradicts authoritative record {rid}')
        if e.get('exit_code')!=rec.get('exit_code'): errors.append(f'execution {eid}: exit_code contradicts authoritative record {rid}')
        if e.get('success_semantics')!=rec.get('success_semantics'): errors.append(f'execution {eid}: success_semantics contradicts authoritative record {rid}')
        rs=rec.get('sut') or {}; rec_sut=entity_by_path_sha(artifacts,rs.get('path'),rs.get('sha256'))
        if len(rec_sut)!=1:
            errors.append(f'execution {eid}: authoritative SUT does not resolve uniquely to graph artifact')
        else:
            graph_sut={(x.get('artifact_id'),x.get('sha256')) for x in e.get('sut',[])}
            expected={(rec_sut[0],rs.get('sha256'))}
            if graph_sut!=expected: errors.append(f'execution {eid}: graph SUT set != authoritative record SUT')
        rt=rec.get('test') or {}; rec_test_sources=entity_by_path_sha(artifacts,rt.get('path'),rt.get('sha256'))
        if len(rec_test_sources)!=1: errors.append(f'execution {eid}: authoritative test source does not resolve uniquely')
        rr=rec.get('result') or {}; rec_results=entity_by_path_sha(evidence,rr.get('path'),rr.get('sha256')) + entity_by_path_sha(artifacts,rr.get('path'),rr.get('sha256'))
        if len(rec_results)!=1: errors.append(f'execution {eid}: authoritative result does not resolve uniquely')
        else:
            if rec_results[0] not in produces_by.get(eid,set()): errors.append(f'execution {eid}: authoritative result is not PRODUCES-linked')
        ex_tests=executes_by.get(eid,set())
        if not ex_tests: errors.append(f'execution {eid}: no EXECUTES relation')
        for tid in ex_tests:
            t=tests.get(tid); sel=selector_for_test.get(tid)
            if not t or not sel: continue
            idx=sel['index']; cmd=rec.get('command') or []
            if idx<0 or idx>=len(cmd) or cmd[idx]!=sel.get('value'):
                errors.append(f'execution {eid}: test {tid} invocation selector does not match authoritative command')
            sources=t.get('source_artifact_ids') or ([t.get('source_artifact_id')] if t.get('source_artifact_id') else [])
            if rec_test_sources and set(sources)!={rec_test_sources[0]}:
                errors.append(f'execution {eid}: test {tid} source identity != authoritative test source')

    kind_specs=profile.get('evidence_kinds',{})
    for eid,e in executions.items():
        rec=record_for_exec.get(eid)
        if not rec: continue
        rr=rec.get('result') or {}
        authoritative_result_ids=entity_by_path_sha(evidence,rr.get('path'),rr.get('sha256')) + entity_by_path_sha(artifacts,rr.get('path'),rr.get('sha256'))
        for b in e.get('evidence_bindings',[]):
            if not isinstance(b,dict): continue
            kind=b.get('kind'); ks=kind_specs.get(kind)
            label=f'execution {eid} binding {kind}'
            if not ks:
                errors.append(f'{label}: evidence kind has no semantic attestation specification'); continue
            if set(b.get('result_entity_ids',[]))!=set(authoritative_result_ids):
                errors.append(f'{label}: binding result identity != authoritative execution result')
                continue
            tid=b.get('test_id'); sel=selector_for_test.get(tid)
            if not sel:
                errors.append(f'{label}: bound test has no invocation selector'); continue
            if sel.get('value') not in ks.get('allowed_selectors',[]):
                errors.append(f'{label}: test selector {sel.get("value")!r} not authorized for evidence kind')
            ent=(evidence.get(authoritative_result_ids[0]) if authoritative_result_ids and authoritative_result_ids[0] in evidence else artifacts.get(authoritative_result_ids[0]) if authoritative_result_ids else None)
            result_obj=load_json_result(package_root,ent,errors,label) if ent else None
            if result_obj is not None:
                for p in ks.get('result_predicates',[]):
                    if not pred_ok(result_obj,p): errors.append(f'{label}: semantic predicate failed {p}')

    for cid,c in claims.items():
        if c.get('state')!='VERIFIED': continue
        for eid in c.get('supported_by',[]):
            if eid not in record_for_exec: errors.append(f'claim {cid}: support execution {eid} lacks authoritative record binding')
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('evidence_graph')
    ap.add_argument('--contract',required=True)
    ap.add_argument('--grammar',required=True)
    ap.add_argument('--model',required=True,help='v0.5-compatible structural model')
    ap.add_argument('--package-root',required=True)
    ap.add_argument('--execution-records',required=True)
    ap.add_argument('--attestation-profile',required=True)
    args=ap.parse_args()
    doc=json.loads(Path(args.evidence_graph).read_text(encoding='utf-8'))
    contract=json.loads(Path(args.contract).read_text(encoding='utf-8'))
    grammar=json.loads(Path(args.grammar).read_text(encoding='utf-8'))
    model=json.loads(Path(args.model).read_text(encoding='utf-8'))
    profile=json.loads(Path(args.attestation_profile).read_text(encoding='utf-8'))
    errs=base.validate(doc,contract,grammar,model,Path(args.package_root))
    errs.extend(semantic_validate(doc,Path(args.package_root),Path(args.execution_records),profile))
    seen=set(); out=[]
    for x in errs:
        if x not in seen: seen.add(x); out.append(x)
    print(json.dumps({'valid':not out,'error_count':len(out),'errors':out},indent=2,ensure_ascii=False))
    raise SystemExit(0 if not out else 1)
if __name__=='__main__': main()
