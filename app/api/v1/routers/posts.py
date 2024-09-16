from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud import posts as posts_crud
from db import db_helper
from schemas.post import (
    PostReadResponse,
    PostCreateRequest,
    PostDeleteResponse,
    PostDeleteRequest,
    PostCreateResponse,
)

router = APIRouter(tags=["Posts"])


# TODO пагинация
@router.get("", response_model=list[PostReadResponse])
async def get_posts(session: Annotated[AsyncSession, Depends(db_helper.get_session)]):
    posts = await posts_crud.get_all_posts(session=session)
    return posts


@router.post("", response_model=PostCreateResponse)
async def create_post(
    session: Annotated[AsyncSession, Depends(db_helper.get_session)],
    post_data: PostCreateRequest,
):
    post = await posts_crud.create_post(session=session, post_to_create=post_data)
    return post


@router.delete("", response_model=PostDeleteResponse)
async def delete_post(
    session: Annotated[AsyncSession, Depends(db_helper.get_session)],
    post_data: PostDeleteRequest,
):
    post = await posts_crud.delete_post(session=session, post_to_delete=post_data)
    return post
