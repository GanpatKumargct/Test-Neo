# Import model modules so SQLAlchemy registers tables with Base.metadata
from app.models import bulk_scan, conversion_log, generated_test  # noqa: F401

__all__ = ["bulk_scan", "conversion_log", "generated_test"]
