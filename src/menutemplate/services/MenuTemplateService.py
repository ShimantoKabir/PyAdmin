from src.menutemplate.repository.MenuTemplateRepository import MenuTemplateRepository
from src.menutemplate.dtos.MenuTemplateCreateRequestDto import MenuTemplateCreateRequestDto
from src.menutemplate.dtos.MenuTemplateCreateResponseDto import MenuTemplateCreateResponseDto
from src.menutemplate.dtos.MenuTemplateResponseDto import MenuTemplateResponseDto
from src.role.dtos.RoleResponseDto import RoleResponseDto
from src.menutemplate.model.MenuTemplate import MenuTemplate;
from src.utils.pagination.PaginationRequestDto import PaginationRequestDto
from src.utils.pagination.PaginationResponseDto import PaginationResponseDto
from src.menutemplate.dtos.MenuTemplateResponseDto import MenuTemplateResponseDto

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
  


  def getById(self, id: int) -> MenuTemplateResponseDto:
    mt = self.repo.getMenuTemplateById(id=id)
    return MenuTemplateResponseDto(
      id=mt.id,
      name=mt.name,
      roleId=mt.roleId,
      roleName=mt.role.name,
      orgId=mt.orgId,
      orgName=mt.org.name,
      tree=mt.tree
    )
  
  def getMenuTemplates(self, reqDto: PaginationRequestDto)->PaginationResponseDto[MenuTemplateResponseDto]:
    total: int|None = reqDto.total
    mtResponseDtoList: list[MenuTemplateResponseDto] = []
    menuTemplates: list[MenuTemplate] = self.repo.getAllMenuTemplate(
      rows=reqDto.rows, 
      page=reqDto.page, 
      orgId=reqDto.orgId
    )

    if reqDto.total is None or reqDto.total == 0:
      total = self.repo.countAllMenuTemplate(orgId=reqDto.orgId)

    for mt in menuTemplates:
      mtDto: MenuTemplateResponseDto = MenuTemplateResponseDto(
        id=mt.id,
        name=mt.name,
        roleId=mt.roleId,
        roleName=mt.role.name,
        orgId=mt.orgId,
        orgName=mt.org.name,
        tree=mt.tree
      )

      mtResponseDtoList.append(mtDto)

    return PaginationResponseDto[RoleResponseDto](items=mtResponseDtoList, total=total)
    
