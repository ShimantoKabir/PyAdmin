from dataclasses import dataclass
from pydantic import constr

@dataclass
class MenuCreateRequestDto:
  label: constr(min_length=1) # type: ignore
  icon: constr(min_length=1) # type: ignore
  href: constr(min_length=1) # type: ignore
