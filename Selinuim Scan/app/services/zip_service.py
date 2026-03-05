"""ZIP extraction and Python file discovery for Selenium test suites."""

import zipfile
from pathlib import Path
from typing import Generator

from app.core.config import settings


def ensure_upload_dir() -> Path:
    """Ensure upload directory exists; return its Path."""
    path = Path(settings.upload_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def extract_zip(zip_path: str | Path, dest_dir: str | Path) -> Path:
    """Extract a ZIP file to dest_dir. Returns dest_dir as Path."""
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(dest)
    return dest


def iter_python_files(root: Path) -> Generator[tuple[Path, str], None, None]:
    """Yield (relative_path, content) for each .py file under root."""
    for path in root.rglob("*.py"):
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            rel = path.relative_to(root)
            yield rel, content
        except Exception:
            continue


def get_python_files_from_zip(zip_path: str | Path) -> list[tuple[str, str]]:
    """
    Extract ZIP to a temp directory, collect all .py (path_str, content), then cleanup.
    Returns list of (relative_path_str, source_code).
    """
    import tempfile
    import shutil

    zip_path = Path(zip_path)
    if not zip_path.is_file():
        return []

    tmp = Path(tempfile.mkdtemp(prefix="selenium_zip_"))
    try:
        extract_zip(zip_path, tmp)
        return [(str(rel), content) for rel, content in iter_python_files(tmp)]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
