from functools import lru_cache
from typing import List, Optional

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

    project_name: str = "Bulk Selenium → NLP Test Case Converter"
    api_v1_prefix: str = "/api/v1"

    # Database
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "selenium_converter"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    @property
    def sqlalchemy_database_uri(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_db}"
        )

    # Celery / Redis
    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/1"
    celery_result_backend: str = "redis://localhost:6379/2"

    # Security / JWT (stubs)
    secret_key: str = "CHANGE_ME_IN_PRODUCTION"
    access_token_expire_minutes: int = 30
    refresh_token_expire_minutes: int = 60 * 24 * 7
    algorithm: str = "HS256"

    # CORS
    cors_origins: List[AnyHttpUrl] = []

    # AI / LLM
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4o"
    gemini_api_key: Optional[str] = None
    gemini_model: str = "gemini-2.5-flash"
    groq_api_key: Optional[str] = None
    groq_model: str = "llama-3.3-70b-versatile"
    ollama_base_url: str = "http://localhost:11434/v1"
    ollama_api_key: str = "ollama"
    ollama_model: str = "deepseek-v3.2:cloud"

    # Observability (stubs)
    sentry_dsn: Optional[str] = None

    # Upload storage (local path; API and worker must share same path or use S3 later)
    upload_dir: str = "uploads"
    max_upload_size_mb: int = 100


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

