from pathlib import Path
from typing import Any

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import PlainTextResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_session
from app.models.bulk_scan import BulkScan
from app.models.generated_test import GeneratedTest
from app.models.conversion_log import ConversionLog
from app.schemas.bulk_scan import BulkScanCreate, BulkScanRead
from app.schemas.conversion_log import ConversionLogRead
from app.schemas.generated_test import GeneratedTestDetail, GeneratedTestRead
from app.services.zip_service import ensure_upload_dir
from app.worker.tasks import enqueue_bulk_conversion


router = APIRouter()

MAX_SIZE_BYTES = (settings.max_upload_size_mb or 100) * 1024 * 1024


@router.post(
    "/upload-zip",
    response_model=BulkScanRead,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Upload Selenium ZIP and start async conversion",
)
async def upload_zip_for_conversion(
    file: UploadFile = File(..., description="ZIP file containing Selenium test suite"),
    session=Depends(get_session),
) -> Any:
    if not file.filename or not file.filename.lower().endswith(".zip"):
        raise HTTPException(status_code=400, detail="Only .zip files are supported")

    # Persist bulk scan metadata first so we have an ID for storage path
    payload = BulkScanCreate(original_filename=file.filename)
    db_obj = payload.to_model()
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)

    # Save ZIP to shared upload dir (API and Celery worker must share this path)
    upload_dir = ensure_upload_dir()
    storage_path = upload_dir / f"{db_obj.id}.zip"
    size = 0
    with open(storage_path, "wb") as f:
        while chunk := await file.read(8192):
            size += len(chunk)
            if size > MAX_SIZE_BYTES:
                storage_path.unlink(missing_ok=True)
                session.delete(db_obj)
                session.commit()
                raise HTTPException(status_code=413, detail=f"File exceeds {settings.max_upload_size_mb} MB limit")
            f.write(chunk)

    db_obj.storage_path = str(storage_path)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)

    # Enqueue Celery task to run conversion in background
    enqueue_bulk_conversion(bulk_scan_id=db_obj.id)

    return BulkScanRead.model_validate(db_obj)


@router.get(
    "/scans/{scan_id}",
    response_model=BulkScanRead,
    summary="Get bulk scan status and metadata",
)
def get_scan(scan_id: int, session: Session = Depends(get_session)) -> Any:
    scan = session.get(BulkScan, scan_id)
    if not scan:
        raise HTTPException(status_code=404, detail="Bulk scan not found")
    return BulkScanRead.model_validate(scan)


@router.get(
    "/scans/{scan_id}/logs",
    response_model=list[ConversionLogRead],
    summary="List conversion logs for a scan (why tests list may be empty)",
)
def list_conversion_logs(scan_id: int, session: Session = Depends(get_session)) -> Any:
    scan = session.get(BulkScan, scan_id)
    if not scan:
        raise HTTPException(status_code=404, detail="Bulk scan not found")
    logs = session.scalars(
        select(ConversionLog).where(ConversionLog.bulk_scan_id == scan_id).order_by(ConversionLog.created_at)
    ).all()
    return [ConversionLogRead.model_validate(log) for log in logs]


@router.get(
    "/scans/{scan_id}/tests",
    response_model=list[GeneratedTestRead],
    summary="List generated TestNeo files for a scan",
)
def list_generated_tests(scan_id: int, session: Session = Depends(get_session)) -> Any:
    scan = session.get(BulkScan, scan_id)
    if not scan:
        raise HTTPException(status_code=404, detail="Bulk scan not found")
    tests = session.scalars(select(GeneratedTest).where(GeneratedTest.bulk_scan_id == scan_id)).all()
    return [GeneratedTestRead.model_validate(t) for t in tests]


@router.get(
    "/scans/{scan_id}/tests/{test_id}",
    response_model=GeneratedTestDetail,
    summary="Get one generated TestNeo file with full content",
)
def get_generated_test(scan_id: int, test_id: int, session: Session = Depends(get_session)) -> Any:
    test = session.get(GeneratedTest, test_id)
    if not test or test.bulk_scan_id != scan_id:
        raise HTTPException(status_code=404, detail="Generated test not found")
    return GeneratedTestDetail.model_validate(test)


@router.get(
    "/scans/{scan_id}/tests/{test_id}/download",
    response_class=PlainTextResponse,
    summary="Download TestNeo content as plain text",
)
def download_testneo(scan_id: int, test_id: int, session: Session = Depends(get_session)) -> PlainTextResponse:
    test = session.get(GeneratedTest, test_id)
    if not test or test.bulk_scan_id != scan_id:
        raise HTTPException(status_code=404, detail="Generated test not found")
    return PlainTextResponse(content=test.testneo_content, media_type="text/plain")

