from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BasePost(BaseModel):
    pass


class PostCreate(BasePost):
    user_id: int
    create_datetime: datetime
    update_datetime: datetime
    text: str


class PostRead(BasePost):
    id: int
    user_id: int
    create_datetime: datetime
    update_datetime: datetime
    text: str


class PostDelete(BasePost):
    user_id: int
    create_datetime: datetime
