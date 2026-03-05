# Bulk Selenium → NLP Test Case Converter (Backend)

Backend service for bulk-converting Selenium-based UI tests into TestNeo-style NLP test cases.

## Stack

- **API**: FastAPI (+ Uvicorn / Gunicorn)
- **DB**: PostgreSQL via SQLAlchemy 2.0 (+ Alembic for migrations)
- **Async**: Celery + Redis
- **Parsing**: Python AST + rule-based TestNeo generator

## Where things run: Docker vs localhost

You can run in two ways:

| What | **Option A: Local dev** (API + worker on your machine) | **Option B: Full Docker** (`docker-compose up`) |
|------|--------------------------------------------------------|-------------------------------------------------|
| **PostgreSQL** | Docker (`docker-compose up -d db redis`) | Docker (service `db`) |
| **Redis** | Docker (same as above) | Docker (service `redis`) |
| **API** (FastAPI) | **Localhost** — `uvicorn app.main:app --reload` | Docker (service `api`) → http://localhost:8000 |
| **Celery worker** | **Localhost** — `celery -A app.worker.celery_app worker ...` | Docker (service `worker`) |
| **Your code / venv** | On your machine; you edit and run API/worker | Only needed to build images; at runtime everything is in containers |

- **Option A:** Use when developing. Only start `db` and `redis` in Docker. Keep `.env` with `POSTGRES_HOST=localhost`, `POSTGRES_PORT=55432`, `REDIS_URL=redis://localhost:6379/0`, etc. Run API and worker in your terminal.
- **Option B:** Use for a single-command run or production-like setup. Run `docker-compose up`; all four services (api, worker, db, redis) run in Docker. The compose file loads `.env` then `.env.docker` (which sets `POSTGRES_HOST=db`, `CELERY_BROKER_URL=redis://redis:6379/1`, etc.) so api/worker connect by service name. If you still see "Connection refused" to Redis or Postgres, run `docker-compose down` then `docker-compose up --force-recreate`.

## Quickstart (Local Dev)

1. **Create virtualenv and install dependencies**

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

2. **Run Postgres & Redis**

Use your own instances or:

```bash
docker-compose up -d db redis
```

Wait a few seconds for Postgres to start, then set `.env` with `POSTGRES_HOST=localhost` (and Redis on `localhost:6379`) when running the API and worker on the host.

3. **Create database tables**

From the project root (with venv active):

```bash
python scripts/create_tables.py
```

Or in one line:

```bash
python -c "from app.db.session import engine; from app.db.base import Base; Base.metadata.create_all(bind=engine)"
```

**If you see "Database connection failed":** Postgres is not reachable. Ensure (1) `docker-compose up -d db` has been run and Postgres is up, (2) `.env` has `POSTGRES_HOST=localhost`, `POSTGRES_USER=postgres`, `POSTGRES_PASSWORD=postgres`, `POSTGRES_DB=selenium_converter`. If you use a local Postgres install (not Docker), create the database first: `createdb -U postgres selenium_converter` (or in `psql`: `CREATE DATABASE selenium_converter;`).

4. **Run the API**

```bash
uvicorn app.main:app --reload
```

5. **Run the Celery worker** (separate terminal, same venv)

```bash
celery -A app.worker.celery_app worker --loglevel=info -Q conversion
```

The worker must have access to the same `uploads` directory as the API (same `UPLOAD_DIR` / working directory when running locally).

## API Overview

- **POST /api/v1/convert/upload-zip** – Upload a ZIP of Selenium Python tests; returns a bulk scan ID (202). Conversion runs asynchronously in the worker.
- **GET /api/v1/convert/scans/{id}** – Get bulk scan status and metadata.
- **GET /api/v1/convert/scans/{id}/logs** – List conversion logs (why the tests list might be empty: no .py in ZIP, or parse errors).
- **GET /api/v1/convert/scans/{id}/tests** – List generated TestNeo files for that scan.
- **GET /api/v1/convert/scans/{id}/tests/{test_id}** – Get one generated test with full content.
- **GET /api/v1/convert/scans/{id}/tests/{test_id}/download** – Download TestNeo content as plain text.

Docs: **http://localhost:8000/api/v1/docs**

## Conversion Pipeline

1. **Upload**: ZIP is saved under `uploads/{scan_id}.zip` and a Celery task is enqueued.
2. **Worker**: Extracts the ZIP, discovers all `.py` files, parses each with Python AST.
3. **AST parser**: Detects Selenium patterns (`driver.get()`, `find_element(By.*, ...)`, `.click()`, `.send_keys()`, `.clear()`, etc.) and builds an ordered list of steps.
4. **TestNeo generator**: Converts steps into natural-language TestNeo format (e.g. “Step 1: Open URL …”, “Step 2: Click on element (id: …)”).
5. **Persistence**: Each converted file is stored as a `GeneratedTest` row; `ConversionLog` entries record errors/info; `BulkScan.status` is set to `completed` or `failed`.

## High-Level Architecture

- `app/main.py` – FastAPI app, routes, middleware
- `app/api/v1/` – Versioned REST endpoints
- `app/core/` – Settings, security, logging
- `app/db/` – Session/engine and base models
- `app/models/` – SQLAlchemy ORM (BulkScan, GeneratedTest, ConversionLog)
- `app/schemas/` – Pydantic request/response schemas
- `app/services/` – `zip_service`, `ast_parser`, `testneo_generator`
- `app/worker/` – Celery app and `run_bulk_conversion` task

Parsing and NLP conversion are implemented with a rule-based engine; the pipeline is ready for iterative enhancement (e.g. more Selenium patterns, LLM enrichment).

