from datetime import datetime

from pydantic import BaseModel


class ConversionLogRead(BaseModel):
    id: int
    bulk_scan_id: int
    level: str
    message: str
    created_at: datetime

    model_config = {"from_attributes": True}
