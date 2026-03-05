from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class GeneratedTest(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    bulk_scan_id: Mapped[int] = mapped_column(ForeignKey("bulkscan.id", ondelete="CASCADE"), index=True)
    source_path: Mapped[str] = mapped_column(String(512), nullable=False)
    testneo_content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    bulk_scan: Mapped["BulkScan"] = relationship("BulkScan", backref="generated_tests")

