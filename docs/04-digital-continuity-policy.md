# Digital Continuity Policy

**Organisation:** NexaTech Solutions (fictional IT services company)
**Version:** 1.0
**Owner:** Records and Information Manager

## 1. Purpose

To make sure the organisation's digital information stays usable, findable and trustworthy for as long as the business, its clients and the law need it, despite changes in technology, systems and staff.

## 2. Scope

This policy covers all digital information created or held by the organisation, including contracts, source code, support records, HR records, design documents, backups, logs and media. It does not cover paper records.

## 3. Principles

1. **Know what we hold.** Every information asset is recorded in the Information Asset Register with an owner, location, format and criticality.
2. **Assess the risk.** Each asset is scored for continuity risk using its file format and criticality.
3. **Keep it as long as needed.** Retention periods are defined by category and reviewed regularly.
4. **Use sustainable formats.** Preferred formats are open and widely supported. Risky formats are migrated.
5. **Check regularly.** The register, risk scores and retention checks are reviewed on a fixed schedule.

## 4. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Records and Information Manager | Owns this policy and the Information Asset Register |
| Asset owners (department heads) | Keep the details of their assets accurate and act on risk findings |
| IT and Infrastructure team | Run backups, migrations and restore tests |
| Compliance and Legal Officer | Confirm retention periods against law and client contracts |
| Senior management | Approve the policy and resource corrective actions |

## 5. Retention schedule

| Category | Retention (years) |
|---|---|
| Contracts | 10 |
| Source code | 10 |
| Customer data | 7 |
| HR records | 7 |
| Support records | 5 |
| Design documents | 5 |
| Documentation | 5 |
| Logs | 3 |
| Media | 3 |
| Backups | 1 |

Categories not listed default to 5 years until the Compliance and Legal Officer sets a period. These periods are illustrative and must be confirmed against actual legal and contractual requirements.

## 6. File format standards

| Type of information | Preferred format | Formats to migrate away from |
|---|---|---|
| Documents | PDF or DOCX | Legacy binary formats |
| Spreadsheets | XLSX or CSV | XLS |
| Databases | SQL export plus CSV | MDB |
| Diagrams | SVG, PDF or VSDX | VSD |
| Video | MP4 | AVI |
| Archives and backups | TAR or ZIP | Proprietary backup formats |
| Logs | Plain text | Proprietary log formats |

## 7. Risk and retention checks

Each asset receives a risk score (format risk x criticality) and a retention status:

| Status | Rule | Required action |
|---|---|---|
| ACTION | Kept 5 or more years and format risk 4 or 5 | Migrate to a preferred format within 90 days |
| REVIEW | Kept 3 or more years and format risk 3 or higher | Asset owner reviews within 6 months |
| OK | Everything else | Review at the next annual check |

## 8. Review cycle

- The Information Asset Register is reviewed every quarter.
- Risk scores and retention checks are rerun every quarter and after any major system change.
- This policy is reviewed once a year.

## 9. Related standards

This policy is informed by ISO 15489 (records management), ISO 14721 (OAIS reference model for digital preservation) and ISO 22301 (business continuity management).