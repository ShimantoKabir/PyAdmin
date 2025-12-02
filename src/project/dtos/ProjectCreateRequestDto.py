from dataclasses import dataclass
from pydantic import constr

@dataclass
class ProjectCreateRequestDto:
  name: constr(min_length=1) # type: ignore
  description: str | None = None
  orgId: int # Required