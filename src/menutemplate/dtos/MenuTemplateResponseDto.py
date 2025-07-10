from dataclasses import dataclass
from pydantic import constr
from src.role.dtos.RoleResponseDto import RoleResponseDto
from src.org.dtos.OrgResDto import OrgResDto

@dataclass
class MenuTemplateResponseDto:
  id: int
  name: str
  role: RoleResponseDto
  org: OrgResDto
  tree: str