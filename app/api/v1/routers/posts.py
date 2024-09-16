from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps.deps import get_db_helper, get_db_helper_session
from crud import posts as posts_crud
from db import db_helper
from models import Post
from schemas.post import PostRead, PostCreate, PostDelete

router = APIRouter(tags=["Posts"])


# TODO пагинация
@router.get("", response_model=list[PostRead])
async def get_posts(session: Annotated[AsyncSession, Depends(get_db_helper_session)]):
    posts = await posts_crud.get_all_posts(session=session)
    return posts


@router.post("", response_model=PostRead)
async def create_post(
    session: Annotated[AsyncSession, Depends(get_db_helper_session)],
    post_data: PostCreate,
) -> Post:
    post = await posts_crud.create_post(session=session, post_to_create=post_data)
    return post


@router.delete("", response_model=PostDelete)
async def delete_post(
    session: Annotated[AsyncSession, Depends(get_db_helper_session)],
    post_data: PostDelete,
) -> Post:
    post = await posts_crud.delete_post(session=session, post_to_delete=post_data)
    return post
