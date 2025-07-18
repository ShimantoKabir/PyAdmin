from dataclasses import dataclass
from pydantic import EmailStr

@dataclass
class UserResponseDto:
  id: int
  email: EmailStr
  verified: bool
  firstName: str
  lastName: str
  contactNumber: str
  disabled: bool
  super: bool