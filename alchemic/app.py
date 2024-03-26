import asyncio

import uvicorn
from fastapi import FastAPI

from alchemic.api.routes import router as api_router
from alchemic.config import settings
from scripts.migrate import migrate_tables, where_to_save_db

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
        print(f'Путь к файлу БД: {where_to_save_db}')
    except Exception as e:
        print(f'Прозошла ошибка: {e}')
    uvicorn.run('alchemic.app:app', reload=True)

