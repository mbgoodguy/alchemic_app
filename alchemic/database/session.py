from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from alchemic.config import settings


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(settings.database_url)
    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            # async with engine.begin() as conn:  # Автоматическое проведение миграций (нежелательно)
            #     await conn.run_sync(Base.metadata.create_all)  # т.к лишние запросы, отсутствие контроля изменений)
            yield session
            await session.commit()
        except exc.SQLAlchemyError as error:
            await session.rollback()
            raise
