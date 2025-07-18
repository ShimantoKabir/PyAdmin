from src.menu.repository.MenuRepository import MenuRepository
from src.menu.dtos.MenuCreateRequestDto import MenuCreateRequestDto
from src.menu.dtos.MenuCreateResponseDto import MenuCreateResponseDto
from src.menu.model.Menu import Menu;
from src.menu.dtos.MenuResponseDto import MenuResponseDto

class MenuService:
  def __init__(self, menuRepository : MenuRepository):
    self.repo = menuRepository

  def createMenu(self, reqDto: MenuCreateRequestDto) -> MenuCreateResponseDto:
    newMenu = self.repo.add(Menu(name=reqDto.name))
    resMenu = MenuCreateResponseDto(id=newMenu.id,name=newMenu.name)
    return resMenu
  
  def getMenus(self)-> list[MenuResponseDto]:
    menuResponseDtoList: list[MenuResponseDto] = []
    menus: list[Menu] = self.repo.getAllRole()

    for m in menus:
      menuDto: MenuResponseDto = MenuResponseDto(
        id=m.id,
        name=m.name
      )

      menuResponseDtoList.append(menuDto)

    return menuResponseDtoList

