import logging
import os
from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine

from database.models import Base

logger = logging.getLogger()
where_to_save_db = Path(__file__).parent.parent / 'db.sqlite3'  # в alchemic (на уровне с README)
print(where_to_save_db)


async def migrate_tables() -> None:
    logger.info("Starting to migrate")

    engine = create_async_engine(f"sqlite+aiosqlite:///{where_to_save_db}")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Done migrating")
