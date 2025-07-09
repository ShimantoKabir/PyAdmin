from sqlmodel import Field, SQLModel

class UserOrgLink(SQLModel, table=True):
  userId: int | None = Field(default=None, foreign_key="userinfo.id", primary_key=True)
  orgId: int | None = Field(default=None, foreign_key="organization.id", primary_key=True)
