from abc import ABC, abstractmethod
from src.menu.model import Menu

class MenuRepository(ABC):
  @abstractmethod
  def getMenuById(self, id: int) -> Menu:
    pass

  @abstractmethod
  def add(self, menu: Menu) -> Menu:
    pass