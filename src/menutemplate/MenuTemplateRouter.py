from fastapi import APIRouter
from src.menutemplate.dtos.MenuTemplateCreateRequestDto import MenuTemplateCreateRequestDto
from src.menutemplate.dtos.MenuTemplateCreateResponseDto import MenuTemplateCreateResponseDto
from src.menutemplate.dtos.MenuTemplateResponseDto import MenuTemplateResponseDto
from di import MenuTemplateServiceDep

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


@routes.get("/menu-templates/{id}", tags=["menu"], name="act:get-menu-template-by-id")
async def getById(id: int, mtService: MenuTemplateServiceDep)-> str:
  return mtService.getById(id)