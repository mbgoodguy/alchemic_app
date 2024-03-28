import logging
from sqlalchemy.ext.asyncio import create_async_engine

from config import postgres_settings
from database.models import Base

logger = logging.getLogger()


async def migrate_tables() -> None:
    logger.info("Starting to migrate")

    engine = create_async_engine(url=postgres_settings.DB_URL)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Done migrating")
