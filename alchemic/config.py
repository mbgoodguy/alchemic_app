import logging
import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)

load_dotenv()


class Settings(BaseSettings):
    """App settings."""

    project_name: str = "alchemist"
    debug: bool = False
    environment: str = "local"

    # Database
    database_url: str = os.getenv('DATABASE_URL')


settings = Settings()
