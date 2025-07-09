from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, DateTime, func

class MenuTemplate(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(default=None, nullable=False)
  roleId: int = Field(default=None, foreign_key="role.id", unique=True)
  role: Optional["Role"] = Relationship(back_populates="menuTemplate") # type: ignore
  orgId: Optional[int] = Field(default=None, foreign_key="organization.id")
  org: Optional["Organization"] = Relationship(back_populates="menuTemplates") # type: ignore
  userId: Optional[int] = Field(default=None, foreign_key="userinfo.id")
  user: Optional["User"] = Relationship(back_populates="menuTemplates") # type: ignore
  tree: str = Field(default=None, nullable=False)
  createdAt: Optional[datetime] = Field(
    sa_column=Column(
      DateTime(timezone=True), server_default=func.now(), nullable=True
    )
  )
  updatedAt: Optional[datetime] = Field(
    sa_column=Column(
      DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
  )
  

