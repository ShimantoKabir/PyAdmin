from dataclasses import dataclass
from pydantic import constr

@dataclass
class MenuTemplateCreateRequestDto:
  name: constr(min_length=1) # type: ignore
  # Removed: roleId
  orgId: int 
  tree: constr(min_length=1) # type: ignore