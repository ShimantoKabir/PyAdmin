from dataclasses import dataclass
from pydantic import constr

@dataclass
class RoleCreateRequestDto:
  name: constr(min_length=1) # type: ignore
  orgId: int # Added: Required to scope the role