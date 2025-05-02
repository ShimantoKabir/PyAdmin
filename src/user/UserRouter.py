from fastapi import APIRouter
from src.user.dtos.UserResponseDto import UserResponseDto
from di import UserServiceDep

routes = APIRouter()

@routes.get("/users/{id}", tags=["user"], name="get-user-by-id", operation_id="1")
async def getById(id: int, userService: UserServiceDep)-> UserResponseDto:
  return userService.getUserById(id)