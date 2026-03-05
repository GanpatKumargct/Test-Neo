from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ConversionLog(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    bulk_scan_id: Mapped[int] = mapped_column(ForeignKey("bulkscan.id", ondelete="CASCADE"), index=True)
    level: Mapped[str] = mapped_column(String(16), default="INFO")
    message: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    bulk_scan: Mapped["BulkScan"] = relationship("BulkScan", backref="logs")

