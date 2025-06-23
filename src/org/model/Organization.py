from sqlmodel import Field, SQLModel, Column, ARRAY, String, Relationship
from typing import List, Optional
from pydantic import HttpUrl
from sqlalchemy import Column, DateTime, func
from datetime import datetime
from src.db.links.UserOrgLinks import UserOrgLink

class Organization(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True, nullable=True)
  domain: str = Field(unique= True, default=None, nullable=True)
  websites: List[HttpUrl] = Field(sa_column=Column(ARRAY(String), nullable=True))
  disabled: bool = Field(default=False , nullable=False)
  users: list["User"] = Relationship(back_populates="orgs", link_model=UserOrgLink) # type: ignore
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