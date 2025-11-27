from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime, func
from datetime import datetime
from typing import Optional

class Bucket(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  expId: int = Field(default=None, nullable=True)
  endUserId: int = Field(default=None, nullable=True)
  variationId: int = Field(default=None, nullable=True)
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