from typing import Sequence
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import Post
from schemas.post import PostCreateRequest, PostDeleteRequest


# TODO нужно ли отдельный класс делать?


async def get_all_posts(session: AsyncSession) -> Sequence[Post]:
    stmt = select(Post).order_by(Post.id)
    # TODO проверить разницу между scalars и execute
    result = await session.scalars(stmt)
    return result.all()


async def create_post(session: AsyncSession, post_to_create: PostCreateRequest) -> Post:
    post = Post(**post_to_create.model_dump())
    post.update_datetime = post.create_datetime
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


async def delete_post(session: AsyncSession, post_to_delete: PostDeleteRequest) -> Post:
    stmt = delete(Post).where(
        Post.user_id == post_to_delete.user_id
        and Post.create_datetime == post_to_delete.create_datetime
    )
    await session.execute(stmt)
    await session.commit()
    return Post(**post_to_delete.model_dump())
