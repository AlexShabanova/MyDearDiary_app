from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Post
from schemas.post import PostCreate


# TODO нужно ли отдельный класс делать?


async def get_all_posts(session: AsyncSession) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    # TODO проверить разницу между scalars и execute
    result = await session.scalars(stmt)
    return result.all()


async def create_post(session: AsyncSession, post_to_create: PostCreate) -> Post:
    post = Post(**post_to_create.model_dump())
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post
