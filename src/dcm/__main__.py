import argparse

from dcm import db


def show_assets():
    rows = db.list_assets()
    print(f"{'ID':<4}{'Name':<28}{'Owner':<20}{'Format':<10}{'Crit':<5}")
    print("-" * 67)
    for r in rows:
        fmt = r["file_format"] or "-"
        print(f"{r['id']:<4}{r['name']:<28}{r['owner']:<20}{fmt:<10}{r['criticality']:<5}")
    print(f"\nTotal: {len(rows)} assets")


def main():
    parser = argparse.ArgumentParser(prog="dcm", description="Digital Continuity Manager")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="create the database")
    sub.add_parser("list", help="show all assets")

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