from dataclasses import dataclass
from pydantic import constr

@dataclass
class ProjectCreateRequestDto:
  name: constr(min_length=1) # type: ignore
  orgId: int # Required (No default value)
  description: str | None = None # Optional (Has default value, so must go last)