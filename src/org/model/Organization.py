from sqlmodel import Field, SQLModel, Relationship, Column, DateTime, func
from typing import Optional
from datetime import datetime
from src.db.links.UserOrgLink import UserOrgLink

class Organization(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True, nullable=True)
  email: str = Field(index=True, nullable=True)
  domain: str = Field(unique=True, default=None, nullable=True)
  disabled: bool = Field(default=False , nullable=False)
  roles: list["Role"] = Relationship(back_populates="org") # type: ignore
  users: list["User"] = Relationship(back_populates="orgs", link_model=UserOrgLink) # type: ignore
  menuTemplates: list["MenuTemplate"] = Relationship(back_populates="org") # type: ignore
  projects: list["Project"] = Relationship(back_populates="org") # type: ignore
  
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