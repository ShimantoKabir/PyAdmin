from src.role.repository.RoleRepository import RoleRepository
from src.role.dtos.RoleCreateRequestDto import RoleCreateRequestDto
from src.role.dtos.RoleCreateResponseDto import RoleCreateResponseDto
from src.role.model.Role import Role;

class RoleService:
  def __init__(self, roleRepository : RoleRepository):
    self.repo = roleRepository

  def createRole(self, reqDto: RoleCreateRequestDto) -> RoleCreateResponseDto:
    newRole = self.repo.add(Role(name=reqDto.name))
    resRole = RoleCreateResponseDto(id=newRole.id,name=newRole.name)
    return resRole