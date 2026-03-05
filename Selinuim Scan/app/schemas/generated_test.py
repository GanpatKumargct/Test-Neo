from datetime import datetime

from pydantic import BaseModel


class GeneratedTestRead(BaseModel):
    id: int
    bulk_scan_id: int
    source_path: str
    created_at: datetime

    model_config = {"from_attributes": True}


class GeneratedTestDetail(GeneratedTestRead):
    testneo_content: str

    model_config = {"from_attributes": True}
