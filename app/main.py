from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import router as api_router
from core.config import settings
from db import db_helper


# works with async context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(api_router, prefix=settings.api.prefix)


# @app.get("/")
# def get_hello():
#     return "Hello world!"


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
