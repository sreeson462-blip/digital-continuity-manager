import argparse

from dcm import db, policy, risk, scanner


def show_assets():
    rows = db.list_assets()
    print(f"{'ID':<4}{'Name':<28}{'Owner':<20}{'Format':<10}{'Crit':<5}")
    print("-" * 67)
    for r in rows:
        fmt = r["file_format"] or "-"
        print(f"{r['id']:<4}{r['name']:<28}{r['owner']:<20}{fmt:<10}{r['criticality']:<5}")
    print(f"\nTotal: {len(rows)} assets")


def show_risk():
    scored = []
    for r in db.list_assets():
        score = risk.risk_score(r["file_format"], r["criticality"])
        scored.append((score, r))
    scored.sort(key=lambda item: item[0], reverse=True)

    print(f"{'ID':<4}{'Name':<28}{'Format':<10}{'Crit':<6}{'Score':<7}{'Level':<8}")
    print("-" * 63)
    for score, r in scored:
        fmt = r["file_format"] or "-"
        level = risk.risk_level(score)
        print(f"{r['id']:<4}{r['name']:<28}{fmt:<10}{r['criticality']:<6}{score:<7}{level:<8}")


def show_retention():
    order = {"ACTION": 0, "REVIEW": 1, "OK": 2}
    results = []
    for r in db.list_assets():
        years = policy.retention_years(r["category"])
        fmt_risk = risk.format_risk(r["file_format"])
        status = policy.retention_status(years, fmt_risk)
        results.append((status, years, fmt_risk, r))
    results.sort(key=lambda item: order[item[0]])

    print(f"{'ID':<4}{'Name':<28}{'Category':<18}{'Format':<10}{'Years':<7}{'FmtRisk':<9}{'Status':<8}")
    print("-" * 84)
    for status, years, fmt_risk, r in results:
        fmt = r["file_format"] or "-"
        print(f"{r['id']:<4}{r['name']:<28}{r['category']:<18}{fmt:<10}{years:<7}{fmt_risk:<9}{status:<8}")


def show_scan(folder):
    results = scanner.scan_folder(folder)
    print(f"{'Name':<26}{'Format':<8}{'Size':<7}{'FmtRisk':<9}{'Checksum':<14}{'Flag':<6}")
    print("-" * 70)
    for f in results:
        fmt = f["format"] or "-"
        flag = "RISKY" if f["format_risk"] >= 4 else "OK"
        print(f"{f['name']:<26}{fmt:<8}{f['size']:<7}{f['format_risk']:<9}{f['sha256'][:12]:<14}{flag:<6}")
    risky = sum(1 for f in results if f["format_risk"] >= 4)
    print(f"\nScanned {len(results)} files, {risky} in risky formats")


def main():
    parser = argparse.ArgumentParser(prog="dcm", description="Digital Continuity Manager")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="create the database")
    sub.add_parser("list", help="show all assets")
    sub.add_parser("risk", help="rank assets by continuity risk")
    sub.add_parser("retention", help="check formats against retention periods")

    scan = sub.add_parser("scan", help="scan a folder and check file formats")
    scan.add_argument("folder", nargs="?", default=str(db.PROJECT_ROOT / "sample_data"))

    add = sub.add_parser("add", help="add a new asset")
    add.add_argument("--name", required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--owner", required=True)
    add.add_argument("--location", required=True)
    add.add_argument("--format", dest="file_format", default=None)
    add.add_argument("--criticality", type=int, required=True, choices=range(1, 6))

    args = parser.parse_args()

    if args.command == "init":
        db.init_db()
        print("Database ready at", db.DB_PATH)
    elif args.command == "list":
        show_assets()
    elif args.command == "risk":
        show_risk()
    elif args.command == "retention":
        show_retention()
    elif args.command == "scan":
        show_scan(args.folder)
    elif args.command == "add":
        db.add_asset(
            args.name,
            args.category,
            args.owner,
            args.location,
            args.file_format,
            args.criticality,
        )
        print(f"Added asset: {args.name}")


if __name__ == "__main__":
    main()