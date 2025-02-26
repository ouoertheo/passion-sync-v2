from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from passion_sync.db import Base
import enum


class ActivityType(str, enum.Enum):
    GENERIC = "generic"


class Activity(Base):
    __tablename__ = "activity"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    created: Mapped[datetime]
    type: Mapped[ActivityType]
    value: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
