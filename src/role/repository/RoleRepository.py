from abc import ABC, abstractmethod
from src.role.model.Role import Role

class RoleRepository(ABC):
  @abstractmethod
  def getRoleById(self, id: int) -> Role:
    pass

  @abstractmethod
  def add(self, role: Role) -> Role:
    pass

  @abstractmethod
  def getAllRole(self, rows: int, page: int, orgId: int) -> list[Role]:
    pass

  @abstractmethod
  def countAllRole(self, orgId: int) -> int:
    pass