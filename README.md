# Digital Continuity Manager

A Python tool that helps an organisation keep its digital information usable, findable and trustworthy over time. Built as a phase-by-phase project for a fictional IT services company, NexaTech Solutions.

## Problem

Organisations store critical information across many systems. Over time, file formats become obsolete, software goes unsupported, and staff leave, so information that is still needed can become unreadable or lost.

## Tech

- Python 3
- SQLite (built-in `sqlite3` module)
- Command-line interface with `argparse`

## Progress

- [x] Day 1: project setup, `assets` table in SQLite
- [x] Day 2: information asset inventory (add, list, sample data, input validation)
- [x] Day 3: risk assessment (format-based scoring, `risk` command, risk document in `docs/`)
- [x] Day 4: policy and retention schedule (`retention` command, policy document in `docs/`)
- [ ] Day 5-6: file scanner and format detection
- [ ] Day 7: testing
- [ ] Day 8: final report

## Usage

Run these from the `src` folder:
    python -m dcm init
    python -m dcm list
    python -m dcm add --name "Employee Handbook" --category "HR records" --owner HR --location SharePoint --format PDF --criticality 2
    python -m dcm risk
    python -m dcm retention

Load 10 sample assets for the fictional company:

    python -m dcm.seed

## Asset fields

| Field | Meaning |
|---|---|
| name | What the asset is |
| category | Type of information (contracts, source code, backups...) |
| owner | Team responsible for it |
| location | System or place where it lives |
| file_format | Format of the data (PDF, XLS, MDB...), used later for obsolescence risk |
| criticality | 1 (low) to 5 (business critical) |