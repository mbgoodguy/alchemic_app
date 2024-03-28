import asyncio

import uvicorn
from fastapi import FastAPI

from alchemic.api.routes import router as api_router
from alchemic.config import settings
from scripts.migrate_psycopg import migrate_tables

app = FastAPI(
    title=settings.project_name,
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.include_router(api_router)

if __name__ == '__main__':
    try:
        asyncio.run(migrate_tables())
        print('Миграции проведены успешно')
    except Exception as e:
        print(f'Прозошла ошибка: {e}')
    uvicorn.run('alchemic.app_postgres_asyncpg:app', reload=True)

