from db import DBSessionDep
from src.org.repository.OrgRepository import OrgRepository
from src.org.model.Organization import Organization
from fastapi import status, HTTPException
from sqlmodel import select


class OrgRepositoryImp(OrgRepository):
  def __init__(self, db: DBSessionDep):
    self.db = db

  def getByDomain(self, domain: str) -> Organization:
    return self.db.exec(select(Organization).filter_by(domain=domain)).first()

  def add(self, org: Organization) -> Organization:
    existOrg = self.getByDomain(org.domain)

    if existOrg:
      raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Organization already exist by this domain!")
    
    self.db.add(org)
    self.db.commit()
    self.db.refresh(org)

    return org