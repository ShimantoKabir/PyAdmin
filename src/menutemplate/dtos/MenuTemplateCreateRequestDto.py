from dataclasses import dataclass
from pydantic import constr

@dataclass
class MenuTemplateCreateRequestDto:
  name: constr(min_length=1) # type: ignore
  roleId: int # required
  orgId: int # required
  tree: constr(min_length=1) # type: ignore