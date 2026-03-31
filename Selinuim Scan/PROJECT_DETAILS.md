# Bulk Selenium → NLP Test Case Converter - Project Details

## Overview
This project is a backend service designed to solve the challenge of migrating legacy test automation scripts. It bulk-converts Selenium-based UI test scripts (written in Python, Java, etc.) into plain natural-language (NLP) test cases formatted for platforms like TestNeo.

Instead of relying solely on brittle AST parsing or regular expressions, the current iteration uses powerful LLMs (like LLaMa-3.3 via Groq) to accurately extract the intent, flow, and exact steps from the code, producing human-readable and structured test instructions.

## Technology Stack

The project uses a modern Python backend stack optimized for asynchronous processing and robust data storage:

- **Web Framework**: FastAPI (with Uvicorn as the ASGI server)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy 2.0 (with Alembic for database migrations)
- **Asynchronous Task Queue**: Celery
- **Message Broker & Result Backend**: Redis
- **AI/Parsing Engine**: OpenAI-compatible Python SDK leveraging Groq API (running the `llama-3.3-70b-versatile` model).
- **Containerization**: Docker & Docker Compose (for database, Redis, and containerized API/worker deployments).

## High-Level Architecture & Flow

The application follows an asynchronous worker pattern due to the latency associated with calling external LLM APIs for multiple files.

1. **Upload Request (Client -> API)**:
   - The user zips a directory containing multiple Selenium automation scripts.
   - The user uploads the ZIP file to the `/api/v1/convert/upload-zip` endpoint.
   - The API saves the ZIP file to local storage, creates a `BulkScan` record in PostgreSQL (with a "pending" status), and pushes a background task to the Celery message queue (in Redis).
   - The API immediately returns an HTTP 202 Accepted with a unique `scan_id`.

2. **Asynchronous Processing (Celery Worker -> LLM -> DB)**:
   - A Celery worker process listening to the `conversion` queue picks up the task.
   - The worker unzips the uploaded file and traverses the directory structure to find the test scripts.
   - For each script found:
     - The code content is read.
     - The code is sent to the **LLM Parser** (`app.services.llm_parser`).
     - The LLaMa-3.3 model processes the raw code with a specific system prompt, expanding loops into individual steps, tracking clicks, inputs, waits, and assertions.
     - The output is returned as formatted, numbered natural-language steps.
     - A `GeneratedTest` record is saved to the database linking back to the parent `BulkScan`.
   - If a file fails to parse, a `ConversionLog` record is written to track the error.
   - Once all files are processed, the worker updates the `BulkScan` status to `completed` (or `failed`).

3. **Status Polling & Retrieval (Client -> API)**:
   - The user polls `/api/v1/convert/scans/{id}` to check if the background conversion task is complete.
   - Once complete, the user calls `/api/v1/convert/scans/{id}/tests` to list all the resulting NLP test case definitions.
   - The test definitions can be individually retrieved or downloaded as text files.
