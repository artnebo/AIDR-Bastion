import json
from functools import lru_cache
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.modules.logger import pipeline_logger


class OpenSearchSettings(BaseModel):
    user: str
    password: str
    host: str
    port: int
    scheme: str = "https"
    pool_size: int = 10


class KafkaSettings(BaseModel):
    bootstrap_servers: str
    topic: str
    security_protocol: str = "PLAINTEXT"
    sasl_mechanism: Optional[str] = None
    sasl_username: Optional[str] = None
    sasl_password: Optional[str] = None
    save_prompt: bool = False


def _load_version() -> str:
    """
    Load version from VERSION file.

    Returns:
        str: Version string from VERSION file, or "unknown" if file not found
    """
    version_path = Path("VERSION")
    if not version_path.exists():
        return "unknown"

    try:
        with open(version_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        pipeline_logger.error(f"Error reading VERSION file: {e}")
        return "unknown"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AIDR Bastion"
    VERSION: str = Field(default_factory=lambda: _load_version())

    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    OS: Optional[OpenSearchSettings] = None
    KAFKA: Optional[KafkaSettings] = None
    PIPELINE_CONFIG: dict = Field(default_factory=dict)

    SIMILARITY_PROMPT_INDEX: str = "similarity-prompt-index"

    SIMILARITY_NOTIFY_THRESHOLD: float = 0.7
    SIMILARITY_BLOCK_THRESHOLD: float = 0.87

    CORS_ORIGINS: list[str] = Field(
        default=["*"],
        env="CORS_ORIGINS",
        description="List of allowed origins for CORS"
    )

    EMBEDDINGS_MODEL: Optional[str] = Field(
        default="nomic-ai/nomic-embed-text-v1.5",
        description="Model for embeddings"
    )

    OPENAI_API_KEY: Optional[str] = Field(
        default="",
        description="API key for OpenAI ChatGPT API"
    )
    OPENAI_MODEL: Optional[str] = Field(
        default="gpt-4",
        description="Default model for OpenAI ChatGPT API"
    )
    OPENAI_BASE_URL: Optional[str] = Field(
        default="https://api.openai.com/v1",
        description="Default base URL for OpenAI ChatGPT API"
    )

    ML_MODEL_PATH: Optional[str] = None


def load_pipeline_config() -> dict:
    """
    Loads pipeline configuration from config.json file.
    Returns raw configuration without instantiating pipelines to avoid circular imports.
    """
    config_path = Path("config.json")
    loaded_config = {}

    if not config_path.exists():
        return loaded_config

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError, KeyError) as e:
        pipeline_logger.error(f"Error reading config.json: {e}")
        return loaded_config


@lru_cache()
def get_settings() -> Settings:
    """
    Returns cached instance of settings.
    Used to avoid reading .env file multiple times.
    """
    settings = Settings()
    settings.PIPELINE_CONFIG = load_pipeline_config()
    return settings
