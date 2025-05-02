from dataclasses import dataclass
from pydantic import EmailStr

@dataclass
class UserResponseDto:
  id: int
  email: EmailStr