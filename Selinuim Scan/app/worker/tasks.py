from pathlib import Path
import tempfile
import shutil

from app.db.session import SessionLocal, session_scope
from app.models.bulk_scan import BulkScan
from app.models.conversion_log import ConversionLog
from app.models.generated_test import GeneratedTest
from app.services.language_detector import detect_language
from app.services.parser_factory import ParserFactory
from app.services.zip_service import extract_zip, iter_test_files
from app.worker.celery_app import celery_app


def enqueue_bulk_conversion(bulk_scan_id: int) -> None:
    run_bulk_conversion.delay(bulk_scan_id)


@celery_app.task(name="app.worker.tasks.run_bulk_conversion", bind=True)
def run_bulk_conversion(self, bulk_scan_id: int) -> None:
    """Extract ZIP, detect language, parse files with correct parser, persist results."""
    session = SessionLocal()
    try:
        bulk_scan = session.get(BulkScan, bulk_scan_id)
        if bulk_scan is None:
            return
        storage_path = bulk_scan.storage_path
    finally:
        session.close()

    zip_path = Path(storage_path).resolve() if storage_path else None
    if not zip_path or not zip_path.is_file():
        with session_scope() as session:
            scan = session.get(BulkScan, bulk_scan_id)
            if scan:
                scan.status = "failed"
                scan.notes = "ZIP file missing or path invalid"
                session.add(ConversionLog(bulk_scan_id=bulk_scan_id, level="ERROR", message=scan.notes))
        return

    tmp_dir = Path(tempfile.mkdtemp(prefix="selenium_worker_"))
    try:
        # 1. Extract
        extract_zip(zip_path, tmp_dir)
        
        # 2. Detect Language
        lang = detect_language(tmp_dir)
        
        # 3. Update BulkScan with detected language
        with session_scope() as session:
            scan = session.get(BulkScan, bulk_scan_id)
            if scan:
                scan.detected_language = lang
                session.add(ConversionLog(bulk_scan_id=bulk_scan_id, level="INFO", message=f"Detected language: {lang}"))
        
        # 4. Get Parser
        parser = ParserFactory.get_parser(lang)
        
        # 5. Process Files
        generated: list[tuple[str, str]] = []
        errors: list[str] = []
        file_count = 0
        
        from app.services.testneo_generator import steps_to_testneo
        
        for rel_path, source in iter_test_files(tmp_dir):
            file_count += 1
            try:
                steps = parser.parse(source)
                title = Path(rel_path).stem.replace("_", " ").title()
                testneo_content = steps_to_testneo(steps, title=title)
                generated.append((str(rel_path), testneo_content))
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
                    message=f"Found {file_count} relevant file(s) in ZIP.",
                )
            )
            for rel_path, content in generated:
                session.add(
                    GeneratedTest(bulk_scan_id=bulk_scan_id, source_path=rel_path, testneo_content=content)
                )
            session.flush()
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
            if file_count == 0:
                bulk_scan.notes = "No supported Selenium test files (.py, .java, .js, .ts, .cs, .kt) found in ZIP"
                session.add(ConversionLog(bulk_scan_id=bulk_scan_id, level="WARNING", message=bulk_scan.notes))
            elif errors:
                bulk_scan.notes = "; ".join(errors[:5])
                if len(errors) > 5:
                    bulk_scan.notes += f" (+{len(errors) - 5} more)"
            
            bulk_scan.status = "completed"
            session.add(bulk_scan)
            
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
