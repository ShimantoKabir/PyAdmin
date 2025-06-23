from sqlmodel import Field, SQLModel

class UserOrgLink(SQLModel, table=True):
  user_id: int | None = Field(default=None, foreign_key="userinfo.id", primary_key=True)
  org_id: int | None = Field(default=None, foreign_key="organization.id", primary_key=True)
