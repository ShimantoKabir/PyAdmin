from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class UserOrgLink(SQLModel, table=True):
  userId: int | None = Field(default=None, foreign_key="userinfo.id", primary_key=True)
  orgId: int | None = Field(default=None, foreign_key="organization.id", primary_key=True)
  
  # 1. Added Role Foreign Key AND Relationship
  roleId: int | None = Field(default=None, foreign_key="role.id")
  role: Optional["Role"] = Relationship(back_populates="userOrgLinks") # type: ignore 

  # 2. Added MenuTemplate Foreign Key AND Relationship
  menuTemplateId: int | None = Field(default=None, foreign_key="menutemplate.id")
  menuTemplate: Optional["MenuTemplate"] = Relationship(back_populates="userOrgLinks") # type: ignore 

  disabled: bool = Field(default=True , nullable=False)
  super: bool = Field(default=False , nullable=False)