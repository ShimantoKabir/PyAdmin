from fastapi import APIRouter
from src.role.dtos.RoleCreateRequestDto import RoleCreateRequestDto
from src.role.dtos.RoleCreateResponseDto import RoleCreateResponseDto
from di import RoleServiceDep

routes = APIRouter()

@routes.post(
  "/role/", 
  response_model= RoleCreateResponseDto, 
  tags=["role"],
  name="act:create-role"
)
async def createRole(
    role: RoleCreateRequestDto,
    roleService: RoleServiceDep
  )->RoleCreateResponseDto:  
  return roleService.createRole(role)