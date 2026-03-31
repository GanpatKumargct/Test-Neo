from pathlib import Path

from app.db.session import SessionLocal, session_scope
from app.models.bulk_scan import BulkScan
from app.models.conversion_log import ConversionLog
from app.models.generated_test import GeneratedTest
from app.services.llm_parser import LLMParser
from app.services.testneo_generator import steps_to_testneo
from app.services.zip_service import get_source_files_from_zip
from app.worker.celery_app import celery_app


def enqueue_bulk_conversion(bulk_scan_id: int) -> None:
    run_bulk_conversion.delay(bulk_scan_id)


@celery_app.task(name="app.worker.tasks.run_bulk_conversion", bind=True)
def run_bulk_conversion(self, bulk_scan_id: int) -> None:
    """Extract ZIP, parse each source with LLM, convert to TestNeo, persist results."""
    session = SessionLocal()
    try:
        bulk_scan = session.get(BulkScan, bulk_scan_id)
        if bulk_scan is None:
            return
        storage_path = bulk_scan.storage_path
    finally:
        session.close()

    # Resolve to absolute path so worker (e.g. in Docker) finds the same file as the API
    zip_path = Path(storage_path).resolve() if storage_path else None
    if not zip_path or not zip_path.is_file():
        with session_scope() as session:
            scan = session.get(BulkScan, bulk_scan_id)
            if scan:
                scan.status = "failed"
                scan.notes = "ZIP file missing or path invalid"
                session.add(ConversionLog(bulk_scan_id=bulk_scan_id, level="ERROR", message=scan.notes))
        return

    pairs = get_source_files_from_zip(zip_path)
    if not pairs:
        with session_scope() as session:
            scan = session.get(BulkScan, bulk_scan_id)
            if scan:
                scan.status = "completed"
                scan.notes = "No Python files found in ZIP"
                session.add(
                    ConversionLog(
                        bulk_scan_id=bulk_scan_id,
                        level="WARNING",
                        message="No source files found in ZIP. Add test files and try again.",
                    )
                )
        return

    generated: list[tuple[str, str]] = []
    errors: list[str] = []

    for rel_path, source in pairs:
        try:
            parser = LLMParser()
            steps = parser.parse(source)
            title = Path(rel_path).stem.replace("_", " ").title()
            if isinstance(steps, str):
                testneo_content = f"# {title}\n\n{steps}"
            else:
                testneo_content = steps_to_testneo(steps, title=title)
            generated.append((rel_path, testneo_content))
        except Exception as e:
            errors.append(f"{rel_path}: {e!s}")

    with session_scope() as session:
        bulk_scan = session.get(BulkScan, bulk_scan_id)
        if not bulk_scan:
            return
        session.add(
            ConversionLog(
                bulk_scan_id=bulk_scan_id,
                level="INFO",
                message=f"Found {len(pairs)} source file(s) in ZIP.",
            )
        )
        for rel_path, content in generated:
            session.add(
                GeneratedTest(bulk_scan_id=bulk_scan_id, source_path=rel_path, testneo_content=content)
            )
        session.flush()  # Persist GeneratedTests so they are visible to the API
        for msg in errors:
            session.add(ConversionLog(bulk_scan_id=bulk_scan_id, level="ERROR", message=msg))
        session.add(
            ConversionLog(
                bulk_scan_id=bulk_scan_id,
                level="INFO",
                message=f"Converted {len(generated)} file(s); {len(errors)} error(s).",
            )
        )
        bulk_scan.status = "completed"
        if errors:
            bulk_scan.notes = "; ".join(errors[:5])
            if len(errors) > 5:
                bulk_scan.notes += f" (+{len(errors) - 5} more)"
        session.add(bulk_scan)
