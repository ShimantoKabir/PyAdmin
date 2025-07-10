from sqlmodel import Field, SQLModel

class UserOrgLink(SQLModel, table=True):
  userId: int | None = Field(default=None, foreign_key="userinfo.id", primary_key=True)
  orgId: int | None = Field(default=None, foreign_key="organization.id", primary_key=True)
  disabled: bool = Field(default=True , nullable=False)
  super: bool = Field(default=False , nullable=False)
