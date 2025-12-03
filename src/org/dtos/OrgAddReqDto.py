from dataclasses import dataclass
from typing import List
from pydantic import constr, EmailStr

@dataclass
class OrgAddReqDto:
  name: constr(min_length=1) # type: ignore
  email: EmailStr
  password: constr(min_length=8) # type: ignore

