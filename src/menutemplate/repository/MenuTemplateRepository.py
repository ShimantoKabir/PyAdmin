from abc import ABC, abstractmethod
from src.menutemplate.model.MenuTemplate import MenuTemplate

class MenuTemplateRepository(ABC):
  @abstractmethod
  def getMenuTemplateById(self, id: int) -> MenuTemplate:
    pass

  @abstractmethod
  def add(self, role: MenuTemplate) -> MenuTemplate:
    pass