from abc import ABC, abstractmethod
from src.role.model.Role import Role

class RoleRepository(ABC):
  @abstractmethod
  def getRoleById(self, id: int) -> Role:
    pass

  @abstractmethod
  def add(self, role: Role) -> Role:
    pass