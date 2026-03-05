from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.bulk_scan import BulkScan


class BulkScanBase(BaseModel):
    original_filename: str


class BulkScanCreate(BulkScanBase):
    def to_model(self) -> BulkScan:
        return BulkScan(original_filename=self.original_filename)


class BulkScanRead(BulkScanBase):
    id: int
    storage_path: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: datetime
    notes: Optional[str] = None

    model_config = {"from_attributes": True}

