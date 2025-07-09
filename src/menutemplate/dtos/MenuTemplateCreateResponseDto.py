from dataclasses import dataclass
from pydantic import constr

@dataclass
class MenuTemplateCreateResponseDto:
  id: int
  name: str
  roleId: int
  orgId: int
  tree: str