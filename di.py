from fastapi import Depends
from typing import Annotated
from src.user.services.UserService import UserService
from src.menu.services.MenuService import MenuService
from db import DBSessionDep
from src.menu.repository.MenuRepositoryImp import MenuRepositoryImp

def getUserService() -> UserService:
  return UserService()

def getMenuService(db: DBSessionDep) -> MenuService:
  repo = MenuRepositoryImp(db)
  return MenuService(repo)

UserServiceDep = Annotated[UserService, Depends(getUserService)]
MenuServiceDep = Annotated[MenuService, Depends(getMenuService)]