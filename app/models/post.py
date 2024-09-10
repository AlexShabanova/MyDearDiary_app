from datetime import datetime
from models import Base
from sqlalchemy.orm import Mapped

from models.mixins.int_id_pk import IntIdPkMixins


class Post(IntIdPkMixins, Base):
    user_id: Mapped[int]
    create_datetime: Mapped[datetime]
    update_datetime: Mapped[datetime]
    text: Mapped[str]
