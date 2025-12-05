from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, DateTime, func

class Role(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(default=None, nullable=True)  
  org: Optional["Organization"] = Relationship(back_populates="roles") # type: ignore 
  orgId: Optional[int] = Field(default=None, foreign_key="organization.id")
  
  # 1. Added relationship back to UserOrgLink
  # This allows you to access role.userOrgLinks to see who has this role
  userOrgLinks: list["UserOrgLink"] = Relationship(back_populates="role") # type: ignore

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