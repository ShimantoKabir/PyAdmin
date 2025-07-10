from abc import ABC, abstractmethod
from src.db.links.UserOrgLink import UserOrgLink

class UserOrgLinkRepository(ABC):
  @abstractmethod
  def edit(self, userId: int, orgId: int) -> UserOrgLink:
    pass

  @abstractmethod
  def get(self, userId: int, orgId: int) -> UserOrgLink:
    pass

