from sqlmodel import Field, SQLModel

class Action(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True)