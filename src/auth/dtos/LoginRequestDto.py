from dataclasses import dataclass
from pydantic import constr

@dataclass
class LoginRequestDto:
  email: constr(min_length=1) # type: ignore
  password: constr(min_length=1) # type: ignore