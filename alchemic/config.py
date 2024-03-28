import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

logging.basicConfig(level=logging.INFO)

load_dotenv()


class Settings:
    """App settings."""

    project_name: str = "alchemist"
    debug: bool = False
    environment: str = "local"

    # Database
    # database_url: str = os.getenv('DATABASE_URL')
    database_url: str = os.getenv('DATABASE_URL')


settings = Settings()


class Postgres_Settings:
    DB_USER = os.getenv('DB_USER')
    DB_HOST = os.getenv('DB_HOST')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')

    DB_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


postgres_settings = Postgres_Settings()
async_engine = create_async_engine(url=postgres_settings.DB_URL, future=True, echo=True)
