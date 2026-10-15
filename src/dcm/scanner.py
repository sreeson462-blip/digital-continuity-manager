import hashlib
from datetime import datetime
from pathlib import Path

from dcm import db, risk


def sha256_of_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def scan_folder(folder):
    results = []
    for path in sorted(Path(folder).rglob("*")):
        if path.is_file():
            ext = path.suffix.lstrip(".").lower() or None
            results.append({
                "path": str(path.resolve()),
                "name": path.name,
                "format": ext,
                "size": path.stat().st_size,
                "sha256": sha256_of_file(path),
                "format_risk": risk.format_risk(ext),
            })
    return results


def compare_and_save(results, folder):
    prefix = str(Path(folder).resolve())
    conn = db.connect()
    known = {
        path: sha
        for path, sha in conn.execute("SELECT path, sha256 FROM files")
        if path.startswith(prefix)
    }
    now = datetime.now().isoformat(timespec="seconds")
    report = {"new": [], "changed": [], "missing": [], "unchanged": []}
    seen = set()

    for f in results:
        seen.add(f["path"])
        if f["path"] not in known:
            report["new"].append(f["name"])
        elif known[f["path"]] != f["sha256"]:
            report["changed"].append(f["name"])
        else:
            report["unchanged"].append(f["name"])
        conn.execute(
            "INSERT INTO files (path, sha256, size, file_format, last_scanned) "
            "VALUES (?, ?, ?, ?, ?) "
            "ON CONFLICT(path) DO UPDATE SET "
            "sha256 = excluded.sha256, size = excluded.size, "
            "file_format = excluded.file_format, last_scanned = excluded.last_scanned",
            (f["path"], f["sha256"], f["size"], f["format"], now),
        )

    for path in known:
        if path not in seen:
            report["missing"].append(Path(path).name)
            conn.execute("DELETE FROM files WHERE path = ?", (path,))

    conn.commit()
    conn.close()
    return report