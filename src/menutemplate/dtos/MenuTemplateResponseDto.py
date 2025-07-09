from dataclasses import dataclass
from pydantic import constr
from src.role.dtos.RoleResponseDto import RoleResponseDto

@dataclass
class MenuTemplateResponseDto:
  id: int
  name: str
  roleId: int
  role: RoleResponseDto
  orgId: int
  tree: str