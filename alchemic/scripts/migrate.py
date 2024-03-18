import asyncio
import logging
import os
from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine

from database.models import Base

logger = logging.getLogger()
where_to_save_db = os.path.join(Path(__file__).parent.parent.parent, 'db.sqlite3')  # в корень проекта


async def migrate_tables() -> None:
    logger.info("Starting to migrate")

    engine = create_async_engine(f"sqlite+aiosqlite:///{where_to_save_db}")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Done migrating")


if __name__ == "__main__":
    try:
        asyncio.run(migrate_tables())
        print('Миграции проведены успешно')
        print(f'Путь к файлу БД: {where_to_save_db}')
    except Exception as e:
        print(f'Прозошла ошибка: {e}')
