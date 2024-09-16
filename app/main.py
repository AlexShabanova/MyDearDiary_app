from contextlib import asynccontextmanager
from typing import Annotated

from fastapi.responses import ORJSONResponse
import uvicorn
from fastapi import FastAPI, Depends
from api import router as api_router
from core.config import settings
from db import db_helper


# works with async context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)  # create_all
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    title="My Dear Diary...",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
