from dataclasses import dataclass
from pydantic import constr

@dataclass
class Token:
  accessToken: constr(min_length=1) # type: ignore
  refreshToken: constr(min_length=1) # type: ignore