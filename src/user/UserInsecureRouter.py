from fastapi import APIRouter
from di import UserServiceDep
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto
from src.user.dtos.UserVerificationRequestDto import UserVerificationRequestDto
from src.user.dtos.UserVerificationResponseDto import UserVerificationResponseDto

routes = APIRouter()

@routes.post(
  "/users/registration", 
  response_model=UserCreateResponseDto, 
  tags=["user"]
)
async def registration(
    reqDto: UserCreateRequestDto,
    userServiceDep: UserServiceDep
  )->UserCreateResponseDto:
  return userServiceDep.createUser(reqDto)

@routes.post("/users/verify", tags=["user"])
async def verify(
    reqDto: UserVerificationRequestDto, 
    userService: UserServiceDep
  )-> UserVerificationResponseDto:
  return userService.verify(reqDto)