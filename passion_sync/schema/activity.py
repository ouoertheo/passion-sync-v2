from datetime import datetime
from pydantic import BaseModel, ConfigDict
from passion_sync.model.activity import ActivityType


class ActivityBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    type: ActivityType
    value: str
    user_id: int


class ActivityCreate(ActivityBase):
    pass


class ActivityResponse(ActivityBase):
    id: int
    created: datetime
