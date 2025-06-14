from fastapi import Depends, BackgroundTasks
from typing import Annotated
from src.user.services.UserService import UserService
from src.menu.services.MenuService import MenuService
from src.auth.services.AuthService import AuthService
from db import DBSessionDep
from src.menu.repository.MenuRepositoryImp import MenuRepositoryImp
from src.user.repository.UserRepositoryImp import UserRepositoryImp
from src.auth.repository.AuthRepositoryImp import AuthRepositoryImp
from src.email.EmailServiceImp import EmailServiceImp
from passlib.context import CryptContext

def getUserService(db: DBSessionDep, bgTask: BackgroundTasks) -> UserService:
  crypto = CryptContext(schemes=["bcrypt"], deprecated="auto")
  repo = UserRepositoryImp(db)
  emailService = EmailServiceImp(bgTask)
  return UserService(repo, crypto, emailService)

def getMenuService(db: DBSessionDep) -> MenuService:
  repo = MenuRepositoryImp(db)
  return MenuService(repo)

def getAuthService(db: DBSessionDep) -> AuthService:
  crypto = CryptContext(schemes=["bcrypt"], deprecated="auto")
  repo = AuthRepositoryImp(db)
  return AuthService(repo, crypto)

UserServiceDep = Annotated[UserService, Depends(getUserService)]
MenuServiceDep = Annotated[MenuService, Depends(getMenuService)]
AuthServiceDep = Annotated[AuthService, Depends(getAuthService)]
