from src.menu.repository.MenuRepository import MenuRepository
from src.menu.model.Menu import Menu
from db import DBSessionDep
from fastapi import status, HTTPException
from sqlmodel import select

class MenuRepositoryImp(MenuRepository):
  def __init__(self, db: DBSessionDep):
    self.db = db

  def getMenuById(self, id: int) -> Menu:
    menu = self.db.get(Menu,id)

    if not menu:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found")
    
    return menu

  def add(self, menu: Menu) -> Menu:
    existMenu = self.db.exec(select(Menu).filter_by(name=menu.name)).first()

    if existMenu:
      raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Menu already exist by this name!")
    
    self.db.add(menu)
    self.db.commit()
    self.db.refresh(menu)

    return menu



  