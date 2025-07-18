from fastapi import APIRouter
from src.menutemplate.dtos.MenuTemplateCreateRequestDto import MenuTemplateCreateRequestDto
from src.menutemplate.dtos.MenuTemplateCreateResponseDto import MenuTemplateCreateResponseDto
from src.menutemplate.dtos.MenuTemplateResponseDto import MenuTemplateResponseDto
from di import MenuTemplateServiceDep
from src.utils.pagination.PaginationRequestDto import PaginationRequestDto
from src.utils.pagination.PaginationResponseDto import PaginationResponseDto

routes = APIRouter()

@routes.post(
  "/menu-templates/", 
  response_model= MenuTemplateCreateResponseDto, 
  tags=["menu"],
  name="act:create-menu-template"
)
async def createRole(
    reqDto: MenuTemplateCreateRequestDto,
    mtService: MenuTemplateServiceDep
  )->MenuTemplateCreateResponseDto:  
  return mtService.createMenuTemplate(reqDto)

@routes.get("/menu-templates/{id}", tags=["menu"], name="act:get-menu-template")
async def getById(id: int, mtService: MenuTemplateServiceDep)-> MenuTemplateResponseDto:
  return mtService.getById(id)

@routes.post(
  "/menu-templates/all",
  tags=["menu"],
  name="act:get-menu-templates",
  response_model=PaginationResponseDto[MenuTemplateResponseDto]
)
async def getMenuTemplates(
  reqDto: PaginationRequestDto, 
  mtService: MenuTemplateServiceDep
) -> PaginationResponseDto[MenuTemplateResponseDto]:  
  return mtService.getMenuTemplates(reqDto)