from abc import ABC, abstractmethod
from src.user.model.User import User

class UserRepository(ABC):
  @abstractmethod
  def getUserById(self, id: int) -> User:
    pass

  @abstractmethod
  def add(self, user: User) -> User:
    pass