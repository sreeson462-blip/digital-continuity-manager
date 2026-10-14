'''
# Risk Assessment

Digital continuity risk assessment for NexaTech Solutions (fictional IT services company), produced with the Digital Continuity Manager tool.

## Method

Each information asset is scored with:

    risk score = format risk x criticality

- **Criticality (impact):** how much the business depends on the asset, rated 1 (low) to 5 (business critical).
- **Format risk (likelihood):** how likely the file format is to become unreadable, rated 1 (very safe) to 5 (very risky).

| Score | Level |
|---|---|
| 15 to 25 | HIGH |
| 8 to 14 | MEDIUM |
| 1 to 7 | LOW |

## Format risk ratings

| Format | Rating | Reason |
|---|---|---|
| PDF | 1 | Open ISO standard, supported everywhere |
| Git | 1 | Open, widely used version control format |
| DOCX | 2 | Open XML format, but closely tied to Microsoft Office |
| TAR | 2 | Simple, open archive format |
| LOG | 2 | Plain text |
| Database | 3 | Depends on database software and version staying available |
| XLS | 3 | Legacy binary Excel format, replaced by XLSX |
| AVI | 4 | Old container format, depends on codecs |
| VSD | 4 | Proprietary binary Visio format, replaced by VSDX |
| MDB | 5 | Legacy Microsoft Access format, replaced by ACCDB |

Formats not in this table receive a default rating of 3.

## Results

| ID | Asset | Format | Criticality | Score | Level |
|---|---|---|---|---|---|
| 10 | Old CRM Export | MDB | 4 | 20 | HIGH |
| 4 | Payroll Records | XLS | 5 | 15 | HIGH |
| 3 | Customer Support Tickets | Database | 4 | 12 | MEDIUM |
| 5 | Architecture Diagrams | VSD | 3 | 12 | MEDIUM |
| 7 | Daily Backups | TAR | 5 | 10 | MEDIUM |
| 8 | Audit Logs | LOG | 4 | 8 | MEDIUM |
| 9 | Marketing Videos | AVI | 2 | 8 | MEDIUM |
| 6 | Project Documentation | DOCX | 3 | 6 | LOW |
| 1 | Client Contracts | PDF | 5 | 5 | LOW |
| 2 | Source Code Repositories | Git | 5 | 5 | LOW |
| 11 | Employee Handbook | PDF | 2 | 2 | LOW |

## Recommended actions

**HIGH**
- Old CRM Export (MDB): migrate to an open format such as CSV or SQL, and move it off the legacy laptop.
- Payroll Records (XLS): convert to XLSX or CSV, and move it off the legacy payroll server.

**MEDIUM**
- Customer Support Tickets: schedule regular exports and test restoring them.
- Architecture Diagrams (VSD): convert to SVG, PDF or VSDX.
- Daily Backups: run restore tests on a schedule.
- Audit Logs: confirm retention rules and archive format.
- Marketing Videos (AVI): re-encode to MP4.

**LOW**
- Review once a year.

## Limitations

This model scores likelihood by file format only. A fuller assessment would also consider software support, storage health, access rights and staff turnover. These can be added in later versions.