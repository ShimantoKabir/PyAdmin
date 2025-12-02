from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, DateTime, func
from datetime import datetime
from typing import Optional
from src.db.links.UserProjectLink import UserProjectLink

class Project(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True, nullable=False)
  description: str = Field(default=None, nullable=True)
  
  # Parent: Organization
  org: Optional["Organization"] = Relationship(back_populates="projects") # type: ignore
  orgId: Optional[int] = Field(default=None, foreign_key="organization.id")

  # Children: Experiments
  experiments: list["Experiment"] = Relationship(back_populates="project") # type: ignore
  
  # Access: Users (via the new link table)
  users: list["User"] = Relationship(back_populates="projects", link_model=UserProjectLink) # type: ignore

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