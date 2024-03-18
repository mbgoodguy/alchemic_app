# run this script for create sqlite database and create migrations in future

import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine

from config import settings
from database.models import Base

logger = logging.getLogger()


async def migrate_tables() -> None:
    logger.info("Starting to migrate")

    engine = create_async_engine(settings.database_url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Done migrating")


if __name__ == "__main__":
    asyncio.run(migrate_tables())
