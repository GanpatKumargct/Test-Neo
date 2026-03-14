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


SUPPORTED_EXTENSIONS = {".py", ".java", ".js", ".ts", ".cs", ".kt"}


def iter_test_files(root: Path) -> Generator[tuple[Path, str], None, None]:
    """Yield (relative_path, content) for each supported test file under root."""
    for path in root.rglob("*"):
        if path.suffix in SUPPORTED_EXTENSIONS:
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
                rel = path.relative_to(root)
                yield rel, content
            except Exception:
                continue


def get_files_from_zip(zip_path: str | Path) -> list[tuple[str, str]]:
    """
    Extract ZIP to a temp directory, collect all supported files (path_str, content), then cleanup.
    Returns list of (relative_path_str, source_code).
    """
    import shutil
    import tempfile

    zip_path = Path(zip_path)
    if not zip_path.is_file():
        return []

    tmp = Path(tempfile.mkdtemp(prefix="selenium_zip_"))
    try:
        extract_zip(zip_path, tmp)
        return [(str(rel), content) for rel, content in iter_test_files(tmp)]
    finally:
        # We don't cleanup yet if we need to detect language first? 
        # Actually, let's keep it simple: extract twice or extract once in the worker.
        shutil.rmtree(tmp, ignore_errors=True)
