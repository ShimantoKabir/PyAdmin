from fastapi import APIRouter
from src.menu.dtos.MenuCreateRequestDto import MenuCreateRequestDto
from src.menu.dtos.MenuCreateResponseDto import MenuCreateResponseDto
from src.menu.dtos.MenuResponseDto import MenuResponseDto
from di import MenuServiceDep

routes = APIRouter()

@routes.post(
  "/menus/", 
  response_model= MenuCreateResponseDto, 
  tags=["menu"],
  name="act:create-menu"
)
async def createMenu(
    reqDto: MenuCreateRequestDto,
    menuService: MenuServiceDep
  )->MenuCreateResponseDto:  
  return menuService.createMenu(reqDto)

@routes.post(
  "/menus/all",
  tags=["menu"],
  name="act:get-menus",
  response_model=list[MenuResponseDto]
)
async def getMenus(
  menuService: MenuServiceDep
) -> list[MenuResponseDto]:  
  return menuService.getMenus()