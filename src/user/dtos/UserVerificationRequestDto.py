from pydantic import EmailStr, constr
from dataclasses import dataclass

@dataclass
class UserVerificationRequestDto:
  otp: constr(min_length=6) # type: ignore
  email: EmailStr
  