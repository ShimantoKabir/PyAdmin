from src.menutemplate.repository.MenuTemplateRepository import MenuTemplateRepository
from src.menutemplate.dtos.MenuTemplateCreateRequestDto import MenuTemplateCreateRequestDto
from src.menutemplate.dtos.MenuTemplateCreateResponseDto import MenuTemplateCreateResponseDto
from src.menutemplate.dtos.MenuTemplateResponseDto import MenuTemplateResponseDto
from src.role.dtos.RoleResponseDto import RoleResponseDto
from src.menutemplate.model.MenuTemplate import MenuTemplate;

class MenuTemplateService:
  def __init__(self, mtRepository : MenuTemplateRepository):
    self.repo = mtRepository

  def createMenuTemplate(self, reqDto: MenuTemplateCreateRequestDto) -> MenuTemplateCreateResponseDto:
    newMt = self.repo.add(MenuTemplate(
      name=reqDto.name,
      orgId=reqDto.orgId,
      roleId=reqDto.roleId,
      tree=reqDto.tree
    ))
    
    resMt = MenuTemplateCreateResponseDto(
      id=newMt.id,
      name=reqDto.name,
      orgId=reqDto.orgId,
      roleId=reqDto.roleId,
      tree=reqDto.tree
    )
    return resMt
  
  def getById(self, id: int) -> str:
    mt = self.repo.getMenuTemplateById(id=id)
    print("mt=",mt.org)
    return "OK"
