import uvicorn
from fastapi import FastAPI


from .config import settings
from .api import router as api_router
app = FastAPI(
    title=settings.project_name,
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run('alchemic.app:app', reload=True)


