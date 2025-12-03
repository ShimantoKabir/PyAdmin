from abc import ABC, abstractmethod
from src.org.model.Organization import Organization

class OrgRepository(ABC):

  @abstractmethod
  def getByDomain(self, domain: str) -> Organization:
    pass

  @abstractmethod
  def add(self, org: Organization) -> Organization:
    pass