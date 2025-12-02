from sqlmodel import Field, SQLModel
from src.db.links.PermissionType import PermissionType


class UserProjectLink(SQLModel, table=True):
  userId: int | None = Field(default=None, foreign_key="userinfo.id", primary_key=True)
  projectId: int | None = Field(default=None, foreign_key="project.id", primary_key=True)
  disabled: bool = Field(default=False, nullable=False)
  super: bool = Field(default=False, nullable=False)
  permissionType: PermissionType = Field(default=PermissionType.VIEWER)