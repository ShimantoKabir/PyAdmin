from fastapi import APIRouter
from di import UserServiceDep
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto

routes = APIRouter()

@routes.post(
  "/users/registration", 
  response_model=UserCreateResponseDto, 
  tags=["user"]
)
async def registration(
    user: UserCreateRequestDto,
    userServiceDep: UserServiceDep
  )->UserCreateResponseDto:
  return userServiceDep.createUser(user)