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
    parser.add_argument("command", choices=["init", "list"], help="init = create database, list = show assets")
    args = parser.parse_args()

    if args.command == "init":
        db.init_db()
        print("Database ready at", db.DB_PATH)
    elif args.command == "list":
        show_assets()


if __name__ == "__main__":
    main()