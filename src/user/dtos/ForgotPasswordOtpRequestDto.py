from dataclasses import dataclass
from pydantic import EmailStr, constr

@dataclass
class ForgotPasswordOtpRequestDto:
  email: EmailStr