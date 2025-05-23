from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime, func

class User(SQLModel, table=True):

  __tablename__ = "userinfo"

  id: int = Field(default=None, primary_key=True)
  email: str = Field(index=True)
  password: str 
  otp: str = Field(default=None, nullable=True)
  verified: bool = Field(default=False , nullable=False)
  disabled: bool = Field(default=False , nullable=False)
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
    
