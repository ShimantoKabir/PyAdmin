from dataclasses import dataclass
from pydantic import EmailStr
from typing import Optional

@dataclass
class UserResponseDto:
  id: int
  email: EmailStr
  verified: bool
  firstName: str
  lastName: str
  contactNumber: str
  disabled: Optional[bool] = None
  super: Optional[str] = None