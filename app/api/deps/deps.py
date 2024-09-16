from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from db import DatabaseHelper


async def get_db_helper() -> DatabaseHelper:
    db_helper = DatabaseHelper(
        url=str(settings.db.url),
        echo=settings.db.echo,
        echo_pool=settings.db.echo_pool,
        pool_size=settings.db.pool_size,
        max_overflow=settings.db.max_overflow,
    )
    return db_helper


async def get_db_helper_session() -> AsyncGenerator[AsyncSession, None]:
    db_helper = await get_db_helper()
    session = db_helper.get_session()
    return session
