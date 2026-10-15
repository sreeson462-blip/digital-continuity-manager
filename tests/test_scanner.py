import hashlib

import pytest

from dcm import db, scanner


@pytest.fixture
def folder(tmp_path, monkeypatch):
    """A temporary database plus an empty folder to scan."""
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test.db")
    db.init_db()
    files = tmp_path / "files"
    files.mkdir()
    return files


def scan(folder):
    results = scanner.scan_folder(folder)
    return scanner.compare_and_save(results, folder)


def test_sha256_of_known_content(folder):
    f = folder / "a.txt"
    f.write_bytes(b"hello")
    assert scanner.sha256_of_file(f) == hashlib.sha256(b"hello").hexdigest()


def test_scan_folder_reports_format_and_risk(folder):
    (folder / "old.mdb").write_text("x")
    results = scanner.scan_folder(folder)
    assert len(results) == 1
    assert results[0]["name"] == "old.mdb"
    assert results[0]["format"] == "mdb"
    assert results[0]["format_risk"] == 5


def test_first_scan_marks_everything_new(folder):
    (folder / "a.pdf").write_text("one")
    (folder / "b.docx").write_text("two")
    changes = scan(folder)
    assert sorted(changes["new"]) == ["a.pdf", "b.docx"]
    assert changes["unchanged"] == []


def test_second_scan_marks_everything_unchanged(folder):
    (folder / "a.pdf").write_text("one")
    scan(folder)
    changes = scan(folder)
    assert changes["unchanged"] == ["a.pdf"]
    assert changes["new"] == []


def test_edited_file_is_changed(folder):
    f = folder / "a.pdf"
    f.write_text("one")
    scan(folder)
    f.write_text("one edited")
    changes = scan(folder)
    assert changes["changed"] == ["a.pdf"]


def test_deleted_file_is_missing(folder):
    f = folder / "a.pdf"
    f.write_text("one")
    scan(folder)
    f.unlink()
    changes = scan(folder)
    assert changes["missing"] == ["a.pdf"]