import uvicorn
from fastapi import FastAPI

from api.routes import router as v1_router
from config import settings

app = FastAPI(
    title=settings.project_name,
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.include_router(v1_router, prefix="/api")


if __name__ == '__main__':
    uvicorn.run('alchemic.app:app', reload=True)


