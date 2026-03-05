"""
Create database tables. Run after Postgres is up and the database exists.

Usage:
  python scripts/create_tables.py

If you see a connection error:
  1. Start Postgres (e.g. docker-compose up -d db) and wait ~5 seconds.
  2. Ensure .env has POSTGRES_HOST=localhost and correct credentials.
  3. If using local Postgres (not Docker), create the DB first:
     createdb -U postgres selenium_converter
     (or in psql: CREATE DATABASE selenium_converter;)
"""

import sys
from pathlib import Path

# Ensure project root is importable when running as a script:
# `python scripts/create_tables.py` sets sys.path[0] to the scripts/ dir.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

def main():
    try:
        from app.db.session import engine
        from app.db.base import Base
        import app.models  # noqa: F401 - registers BulkScan, GeneratedTest, ConversionLog with Base.metadata
    except Exception as e:
        print("Failed to import app:", e, file=sys.stderr)
        sys.exit(1)

    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
    except Exception as e:
        print("Database connection failed:", file=sys.stderr)
        print(e, file=sys.stderr)
        print("\nCheck:", file=sys.stderr)
        print("  1. Postgres is running (e.g. docker-compose up -d db)", file=sys.stderr)
        print("  2. .env has POSTGRES_HOST=localhost, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB", file=sys.stderr)
        print("  3. Database 'selenium_converter' exists (Docker creates it from POSTGRES_DB)", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
