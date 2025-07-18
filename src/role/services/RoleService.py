from src.role.repository.RoleRepository import RoleRepository
from src.role.dtos.RoleCreateRequestDto import RoleCreateRequestDto
from src.role.dtos.RoleCreateResponseDto import RoleCreateResponseDto
from src.role.model.Role import Role;
from src.utils.pagination.PaginationRequestDto import PaginationRequestDto
from src.utils.pagination.PaginationResponseDto import PaginationResponseDto
from src.role.dtos.RoleResponseDto import RoleResponseDto

class RoleService:
  def __init__(self, roleRepository : RoleRepository):
    self.repo = roleRepository

  def createRole(self, reqDto: RoleCreateRequestDto) -> RoleCreateResponseDto:
    newRole = self.repo.add(Role(name=reqDto.name))
    resRole = RoleCreateResponseDto(id=newRole.id,name=newRole.name)
    return resRole
  
  def getRoles(self, reqDto: PaginationRequestDto)->PaginationResponseDto[RoleResponseDto]:
    total: int|None = reqDto.total
    roleResponseDtoList: list[RoleResponseDto] = []
    roles: list[Role] = self.repo.getAllRole(rows=reqDto.rows, page=reqDto.page, orgId=reqDto.orgId)

    if reqDto.total is None or reqDto.total == 0:
      total = self.repo.countAllRole(orgId=reqDto.orgId)

    for r in roles:
      roleDto: RoleResponseDto = RoleResponseDto(
        id=r.id,
        name=r.name
      )

      roleResponseDtoList.append(roleDto)

    return PaginationResponseDto[RoleResponseDto](items=roleResponseDtoList, total=total)