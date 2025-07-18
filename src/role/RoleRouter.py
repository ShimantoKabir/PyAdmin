from fastapi import APIRouter
from src.role.dtos.RoleCreateRequestDto import RoleCreateRequestDto
from src.role.dtos.RoleCreateResponseDto import RoleCreateResponseDto
from di import RoleServiceDep
from src.utils.pagination.PaginationRequestDto import PaginationRequestDto
from src.utils.pagination.PaginationResponseDto import PaginationResponseDto
from src.role.dtos.RoleResponseDto import RoleResponseDto

routes = APIRouter()

@routes.post(
  "/roles/", 
  response_model= RoleCreateResponseDto, 
  tags=["role"],
  name="act:create-role"
)
async def createRole(
    role: RoleCreateRequestDto,
    roleService: RoleServiceDep
  )->RoleCreateResponseDto:  
  return roleService.createRole(role)


@routes.post(
  "/roles/all",
  tags=["role"],
  name="act:get-roles",
  response_model=PaginationResponseDto[RoleResponseDto]
)
async def getRoles(
  reqDto: PaginationRequestDto, 
  roleService: RoleServiceDep
) -> PaginationResponseDto[RoleResponseDto]:  
  return roleService.getRoles(reqDto)