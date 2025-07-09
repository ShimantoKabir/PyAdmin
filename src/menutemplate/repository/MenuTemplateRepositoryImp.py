from src.menutemplate.repository.MenuTemplateRepository import MenuTemplateRepository
from src.menutemplate.model.MenuTemplate import MenuTemplate
from db import DBSessionDep
from fastapi import status, HTTPException
from sqlmodel import select

class MenuTemplateRepositoryImp(MenuTemplateRepository):
  def __init__(self, db: DBSessionDep):
    self.db = db

  def getMenuTemplateById(self, id: int) -> MenuTemplate:
    mt = self.db.get(MenuTemplate,id)

    if not mt:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu template not found")
    
    return mt

  def add(self, mt: MenuTemplate) -> MenuTemplate:    
    self.db.add(mt)
    self.db.commit()
    self.db.refresh(mt)

    return mt



  