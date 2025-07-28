from sqlmodel import Field, SQLModel

class Menu(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  label: str = Field(default=None, index=True, nullable=True)
  icon:  str = Field(default=None, nullable=True)
  href: str = Field(default=None, nullable=True)


    
