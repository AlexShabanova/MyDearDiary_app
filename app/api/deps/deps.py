from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from db import DatabaseHelper, db_helper


async def get_db_helper() -> DatabaseHelper:
    return db_helper


async def get_db_helper_session(
    db_helper_instance: Annotated[DatabaseHelper, Depends(get_db_helper)]
) -> AsyncGenerator[AsyncSession, None]:
    session = db_helper_instance.get_session()
    print(type(session))
    return session
