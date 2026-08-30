# Attendance burn v0.2

This stage converts the initial static/reverse-engineering findings into executed falsification.

Key results:

- `R-04`: deterministic close/edit race reproduced **20/20** against the unmodified production `RoomAttendanceRepository.kt` source.
- `X-03`: negative control proves that same-instance reread can pass while state disappears after repository recreation.
- Evidence states are separated as `DECLARED`, `IMPLEMENTED`, `REACHABLE`, `TEST_AUTHORED`, `EXECUTED`, `PASSED`, `VERIFIED` rather than treated as automatic implications.
- `G v0.1.1` remains untouched.

Exact source specimen and archive identities are pinned in `specimens/SHA256SUMS.md`; the complete v0.2 working package is preserved inside the integrated snapshot under `archive/`.
