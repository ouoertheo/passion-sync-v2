from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from passion_sync.db import Base
from passion_sync.model.activity import Activity


class Couple(Base):
    __tablename__ = "couple"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    users: Mapped[Optional[list["User"]]] = relationship()


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    couple_id: Mapped[Optional[int]] = mapped_column(ForeignKey("couple.id"))

    activities: Mapped[list[Activity]] = relationship()
