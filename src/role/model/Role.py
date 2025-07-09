from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class Role(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True)
  menuTemplate: Optional["MenuTemplate"] = Relationship(back_populates="role") # type: ignore
    
