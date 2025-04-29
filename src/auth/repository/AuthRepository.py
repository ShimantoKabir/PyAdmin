from abc import ABC, abstractmethod
from src.user.model.User import User

class AuthRepository(ABC):
  
  @abstractmethod
  def getUserByEmail(self, email: str) -> User:
    pass