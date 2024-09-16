from datetime import datetime
from pydantic import BaseModel


class BasePost(BaseModel):
    user_id: int
    create_datetime: datetime


class BasePostRequest(BasePost):
    pass


class BasePostResponse(BasePost):
    pass


class PostCreateRequest(BasePostRequest):
    text: str


class PostReadRequest(BasePostRequest):
    id: int
    update_datetime: datetime
    text: str


class PostDeleteRequest(BasePostResponse):
    pass


class PostCreateResponse(BasePostResponse):
    update_datetime: datetime
    text: str


class PostReadResponse(BasePostResponse):
    id: int
    update_datetime: datetime
    text: str


class PostDeleteResponse(BasePostResponse):
    pass
