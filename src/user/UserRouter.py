from fastapi import APIRouter
from db import DBSessionDep
from di import UserServiceDep
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto

routes = APIRouter()

@routes.post("/users/", response_model=UserCreateResponseDto, tags=["create-user"])
async def createUser(
    user: UserCreateRequestDto,
    userServiceDep: UserServiceDep,
    dbSessionDep: DBSessionDep
  )->UserCreateResponseDto:
  return userServiceDep.createUser(user,dbSessionDep)