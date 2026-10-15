import hashlib
from pathlib import Path

from dcm import risk


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
                "name": path.name,
                "format": ext,
                "size": path.stat().st_size,
                "sha256": sha256_of_file(path),
                "format_risk": risk.format_risk(ext),
            })
    return results