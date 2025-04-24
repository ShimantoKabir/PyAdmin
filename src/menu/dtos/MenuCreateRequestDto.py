from dataclasses import dataclass
from pydantic import constr

@dataclass
class MenuCreateRequestDto:
  name: constr(min_length=1) # type: ignore
