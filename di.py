from fastapi import Depends
from typing import Annotated
from src.user.services.UserService import UserService

def getUserService() -> UserService:
  return UserService()

UserServiceDep = Annotated[UserService, Depends(getUserService)]