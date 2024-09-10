from datetime import datetime
from pydantic import BaseModel


class BasePost(BaseModel):
    user_id: int
    create_datetime: datetime
    update_datetime: datetime
    text: str


class PostCreate(BasePost):
    pass


class PostRead(BasePost):
    id: int
