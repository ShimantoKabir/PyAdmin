from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, DateTime, func

class Role(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True)
  menuTemplate: Optional["MenuTemplate"] = Relationship(back_populates="role") # type: ignore
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
    
