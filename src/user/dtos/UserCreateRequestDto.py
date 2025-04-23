from dataclasses import dataclass
from pydantic import EmailStr, constr

@dataclass
class UserCreateRequestDto:
  password: constr(min_length=1) # type: ignore
  email: EmailStr