from dataclasses import dataclass
from pydantic import constr

@dataclass
class AuthRefreshRequestDto:
  refreshToken: constr(min_length=1) # type: ignore