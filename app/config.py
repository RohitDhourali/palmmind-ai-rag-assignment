
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openrouter_api_key: str
    redis_host: str
    redis_port: int
    qdrant_host: str
    qdrant_port: int
    model_name: str

    class Config:
        env_file = ".env"

settings = Settings()