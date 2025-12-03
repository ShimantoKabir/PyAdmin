from fastapi import Depends, BackgroundTasks
from typing import Annotated
from src.user.services.UserService import UserService
from src.menu.services.MenuService import MenuService
from src.auth.services.AuthService import AuthService
from src.role.services.RoleService import RoleService
from src.menutemplate.services.MenuTemplateService import MenuTemplateService
from db import DBSessionDep
from src.menu.repository.MenuRepositoryImp import MenuRepositoryImp
from src.user.repository.UserRepositoryImp import UserRepositoryImp
from src.auth.repository.AuthRepositoryImp import AuthRepositoryImp
from src.role.repository.RoleRepositoryImp import RoleRepositoryImp
from src.menutemplate.repository.MenuTemplateRepositoryImp import MenuTemplateRepositoryImp
from src.org.repository.OrgRepositoryImp import OrgRepositoryImp
from src.db.repository.UserOrgLinkRepositoryImp import UserOrgLinkRepositoryImp
from src.email.EmailServiceImp import EmailServiceImp
from passlib.context import CryptContext
from src.project.services.ProjectService import ProjectService
from src.project.repository.ProjectRepositoryImp import ProjectRepositoryImp
from src.db.repository.UserProjectLinkRepositoryImp import UserProjectLinkRepositoryImp
from src.org.services.OrgService import OrgService
from src.utils.FileService import FileService

def getUserService(db: DBSessionDep, bgTask: BackgroundTasks) -> UserService:
  crypto = CryptContext(schemes=["bcrypt"], deprecated="auto")
  userRepo = UserRepositoryImp(db)
  orgRepo = OrgRepositoryImp(db)
  userOrgLinkRepo = UserOrgLinkRepositoryImp(db)
  emailService = EmailServiceImp(bgTask)
  return UserService(userRepo, orgRepo, userOrgLinkRepo, crypto, emailService)

def getMenuService(db: DBSessionDep) -> MenuService:
  repo = MenuRepositoryImp(db)
  return MenuService(repo)

def getRoleService(db: DBSessionDep) -> RoleService:
  repo = RoleRepositoryImp(db)
  return RoleService(repo)

def getMenuTemplateService(db: DBSessionDep) -> MenuTemplateService:
  repo = MenuTemplateRepositoryImp(db)
  return MenuTemplateService(repo)

def getAuthService(db: DBSessionDep) -> AuthService:
  crypto = CryptContext(schemes=["bcrypt"], deprecated="auto")
  repo = AuthRepositoryImp(db)
  return AuthService(repo, crypto)

def getProjectService(db: DBSessionDep) -> ProjectService:
  projectRepo = ProjectRepositoryImp(db)
  linkRepo = UserProjectLinkRepositoryImp(db)
  return ProjectService(projectRepo, linkRepo)

def getFileService() -> FileService:
  return FileService()

def getOrgService(db: DBSessionDep, bgTask: BackgroundTasks) -> OrgService:
  orgRepo = OrgRepositoryImp(db)
  userRepo = UserRepositoryImp(db)
  roleRepo = RoleRepositoryImp(db)
  crypto = CryptContext(schemes=["bcrypt"], deprecated="auto")
  fileService = getFileService()
  emailService = EmailServiceImp(bgTask)
  return OrgService(orgRepo, userRepo, roleRepo, crypto, fileService, emailService)

UserServiceDep = Annotated[UserService, Depends(getUserService)]
MenuServiceDep = Annotated[MenuService, Depends(getMenuService)]
AuthServiceDep = Annotated[AuthService, Depends(getAuthService)]
RoleServiceDep = Annotated[RoleService, Depends(getRoleService)]
MenuTemplateServiceDep = Annotated[MenuTemplateService, Depends(getMenuTemplateService)]
ProjectServiceDep = Annotated[ProjectService, Depends(getProjectService)]
OrgServiceDep = Annotated[OrgService, Depends(getOrgService)]

