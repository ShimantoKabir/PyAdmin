from dataclasses import dataclass
from pydantic import EmailStr

@dataclass
class UserCreateResponseDto:
  id: int
  email: EmailStr
  message: str