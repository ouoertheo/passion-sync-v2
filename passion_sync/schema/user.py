from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from passion_sync.schema.activity import ActivityResponse


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    
class UserActivitiesResponse(UserBase):
    id: int
    activities: list[ActivityResponse]


class UserQuery(BaseModel):
    name: Optional[str] = ""
    id: Optional[int] = 0


class CoupleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    users: Optional[list[UserBase]] = Field(default_factory=list)


class CoupleCreate(CoupleBase):
    pass


class CoupleResponse(CoupleBase):
    id: int
