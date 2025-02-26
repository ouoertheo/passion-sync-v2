from passion_sync.db import Session
from passion_sync.model.user import Couple, User

from psycopg2.errors import UniqueViolation

from sqlalchemy.exc import IntegrityError
import sqlalchemy.orm as orm
from sqlalchemy import select

from fastapi import status, HTTPException


def create_user(name):
    try:
        with Session.begin() as session:
            session.expire_on_commit = False
            user = User(name=name)
            session.add(user)
            return user
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail=f"User exists"
            )


def get_user(id: int):
    try:
        with Session() as session:
            statement = select(User).filter_by(id=id)
            user = session.scalar(statement=statement)
            return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)


def list_users():
    try:
        with Session() as session:
            statement = select(User)
            users = session.scalars(statement).all()
            return users
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


def list_user_activities(user_id: int):
    try:
        with Session() as session:
            session.expire_on_commit = False
            statement = (
                select(User)
                .options(orm.joinedload(User.activities))
                .filter_by(id=user_id)
            )
            user = session.scalar(statement)
            return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


def create_couple(name: str, users: list[User] = []):
    try:
        with Session.begin() as session:
            session.expire_on_commit = False
            couple = Couple(name=name, users=users)
            session.add_all([couple] + users)
            return couple
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail=f"Couple exists"
            )
