from fastapi import APIRouter, HTTPException, status, Depends, Query
import sqlalchemy.orm as orm
import passion_sync.service.user as user
import passion_sync.db as db
from passion_sync.schema.user import UserCreate, UserResponse, UserActivitiesResponse
from passion_sync.schema.user import CoupleCreate, CoupleResponse

user_router = APIRouter(prefix="/user", tags=["Users"])


@user_router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    return user.create_user(user.name)


@user_router.get(
    "/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK
)
def get_user(user_id: int):
    user = user.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@user_router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def list_users():
    users = user.list_users()
    return users


@user_router.get("/{user_id}/activities", response_model=UserActivitiesResponse, status_code=status.HTTP_200_OK)
def list_user_activities(user_id: int):
    user = user.list_user_activities(user_id)
    return user


####################################
########## COUPLE ROUTING ##########
####################################

couple_router = APIRouter(prefix="/couple", tags=["Users"])


@couple_router.post("/", response_model=CoupleResponse, status_code=201)
def create_couple(couple: CoupleCreate):
    return user.create_couple(couple.name)
