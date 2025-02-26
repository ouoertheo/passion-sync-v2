from fastapi import APIRouter, HTTPException, status
import passion_sync.service.activity as activity_service
from passion_sync.schema.activity import (
    ActivityCreate,
    ActivityResponse,
    ActivityType,
)

activity_router = APIRouter(prefix="/activity", tags=["Activity"])


@activity_router.post(
    path="/", response_model=ActivityResponse, status_code=status.HTTP_201_CREATED
)
def create_activity(activity: ActivityCreate):
    return activity_service.add_activity(activity)


@activity_router.get(
    "/{activity_id}", response_model=ActivityResponse, status_code=status.HTTP_200_OK
)
def get_activity(activity_id: int):
    activity = activity_service.get_activity(activity_id)
    if not activity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found"
        )
    return activity


@activity_router.get(
    "/", response_model=list[ActivityResponse], status_code=status.HTTP_200_OK
)
def list_activities():
    activities = activity_service.list_activities()
    return activities
