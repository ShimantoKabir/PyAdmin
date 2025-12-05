from dataclasses import dataclass
from pydantic import constr, EmailStr

@dataclass
class OrgAddReqDto:
  # 1. The email of the existing user to add
  email: EmailStr
  
  # 2. The domain of the organization to add them to
  domain: constr(min_length=1) # type: ignore
  
  # 3. Permissions are mandatory when adding a user
  roleId: int
  menuTemplateId: int