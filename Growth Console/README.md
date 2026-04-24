# TestNeo Growth Console

A lightweight internal sales tool that helps the TestNeo team collect leads, prioritize them using AI, generate personalized outreach messages, and track their progress through a pipeline.

## Features
- **Lead Management**: Add, update, and manage leads in a pipeline.
- **AI Scoring**: Automatically score leads (1-10) based on their relevance using LangChain and Groq LLM.
- **AI Email Generation**: Automatically generate highly personalized outreach emails using the lead's role, company, and notes.
- **Dashboard**: Track overall progress across different pipeline stages (Contacted, Replied, Converted).
- **Dockerized**: Fully containerized setup for easy local execution.

## Architecture
The application follows a clean Domain-Driven Design (DDD) architecture and is split into two primary components:
- **Frontend**: Streamlit-based user interface.
- **Backend**: FastAPI-based REST API, handling SQLite operations and AI integrations (Groq LLM).
- **Database**: PostgreSQL database.

## Prerequisites
- Docker
- Docker Compose
- Groq API Key (for AI capabilities)

## Setup & Execution

1. **Environment Variables**:
Create a `.env` file in the root folder or set the `GROQ_API_KEY` environment variable on your system:
```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

2. **Run with Docker Compose**:
Navigate to the root directory and start the services:
```bash
docker-compose -f docker/docker-compose.yml up --build
```

3. **Access the Application**:
- **Frontend**: http://localhost:8501
- **Backend API Docs**: http://localhost:8000/docs
- **Database**: Port 5432 (mapped to local)

## Note on AI Fallback
If the `GROQ_API_KEY` is not provided or fails to initialize, the application will gracefully fall back to returning mocked AI responses, ensuring you can still test the pipeline flow.

🚀 How to Run It
First, navigate to the root directory in your terminal:
powershell
cd "e:\Test Neo\Growth Console"
(Optional but recommended) Set your Groq API Key as an environment variable in your terminal:
powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
Spin up the application using Docker Compose:
powershell
docker-compose -f docker/docker-compose.yml up --build
Access Points:
Streamlit App (UI): http://localhost:8501
FastAPI Swagger Docs: http://localhost:8000/docs
Database: Port 5432 mapped locally