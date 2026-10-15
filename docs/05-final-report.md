# Final Report: Digital Continuity Management at NexaTech Solutions

## Purpose
NexaTech Solutions is a fictional IT company. This project is a Python and SQLite
command-line tool that helps it keep its digital information usable over time.
It tracks information assets, scores the risk of losing access to them,
applies a retention policy, and checks files for damage or change.

## What the tool does
| Area | Feature | Command |
|------|---------|---------|
| Asset register | Record each asset with owner, location, format and criticality | `python -m dcm add`, `list` |
| Risk assessment | Score = format risk (1-5) x criticality (1-5); HIGH >= 15, MEDIUM 8-14, LOW < 8 | `python -m dcm risk` |
| Retention policy | Retention years per category; flags ACTION or REVIEW | `python -m dcm retention` |
| Fixity checking | SHA-256 checksums; reports new, changed and missing files | `python -m dcm scan` |
| Testing | 16 automated pytest tests | `python -m pytest` |

## Findings
Register of 11 assets:

- Risk levels: 2 HIGH, 5 MEDIUM, 4 LOW.
- The highest risk is **Old CRM Export** (MDB format, score 20), followed by
  **Payroll Records** (XLS format, score 15).
- Retention status: 2 need ACTION, 3 need REVIEW and 6 are OK.
- ACTION items: **Old CRM Export** (kept 7 years in MDB) and
  **Architecture Diagrams** (kept 5 years in VSD).
- A scan of the sample folder found 8 files, 3 in risky formats
  (MDB, VSD, AVI).
- Change detection was tested by editing one file, deleting one and adding one;
  all three changes were reported correctly.

## Recommendations
1. Migrate the Old CRM Export from MDB to an open format such as SQLite or CSV.
2. Export Architecture Diagrams from VSD to PDF or SVG alongside the originals.
3. Review Payroll Records (XLS) and keep a CSV or PDF copy for the 7-year retention.
4. Re-scan on a regular schedule so changed and missing files are caught early.

## Technology
Python 3, SQLite (`sqlite3`), `argparse`, `hashlib` (SHA-256), `pathlib`, pytest, Git and GitHub.

## Limitations and future work
- The format risk table is a fixed list and should be reviewed regularly.
- The scanner detects change but does not say whether a change was intended.
- Possible next steps: scheduled scans, CSV export of reports, a web dashboard.