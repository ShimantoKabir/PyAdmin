from fastapi import APIRouter
from src.menu.dtos.MenuCreateRequestDto import MenuCreateRequestDto
from src.menu.dtos.MenuCreateResponseDto import MenuCreateResponseDto
from di import MenuServiceDep
from db import DBSessionDep

routes = APIRouter()

@routes.post("/menus/", response_model= MenuCreateResponseDto, tags=["create-menu"])
async def createMenu(
    menu: MenuCreateRequestDto,
    menuService: MenuServiceDep
  )->MenuCreateResponseDto:  
  return menuService.createMenu(menu)