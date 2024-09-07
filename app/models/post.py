from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer

from models import Base
from sqlalchemy.orm import Mapped


# TODO попробовать создать таблицу из main
# class Post(Base):
#     user_id = Column(Integer)
#     create_datetime = Column(DateTime)
#     update_datetime = Column(DateTime)
#     text = Column(String)


class Post(Base):
    user_id: Mapped[int]
    create_datetime: Mapped[datetime]
    update_datetime: Mapped[datetime]
    text: Mapped[str]
