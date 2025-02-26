from datetime import datetime

from passion_sync.db import Session
from passion_sync.model.activity import Activity, ActivityType
from passion_sync.model.user import User
from passion_sync.schema.activity import ActivityCreate
import passion_sync.metrics as metrics

from psycopg2.errors import UniqueViolation
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from fastapi import status, HTTPException


def add_activity(activity: ActivityCreate):
    try:
        with Session.begin() as session:
            session.expire_on_commit = False
            new_activity = Activity(
                type=activity.type, value=activity.value, created=datetime.now()
            )
            statement = select(User).filter_by(id=activity.user_id)
            user = session.scalar(statement=statement)
            user.activities.append(new_activity)
            session.add_all([new_activity, user])
            metrics.add_activity(user, new_activity)
            return new_activity
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail=f"Activity exists"
            )


def get_activity(id: int):
    try:
        with Session() as session:
            statement = select(Activity).filter_by(id=id)
            activity = session.scalar(statement=statement)
            return activity
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)


def list_activities():
    try:
        with Session() as session:
            statement = select(Activity)
            activities = session.scalars(statement=statement).all()
            return activities
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

