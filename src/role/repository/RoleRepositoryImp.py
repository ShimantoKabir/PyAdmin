from src.role.repository.RoleRepository import RoleRepository
from src.role.model.Role import Role
from db import DBSessionDep
from fastapi import status, HTTPException
from sqlmodel import select

class RoleRepositoryImp(RoleRepository):
  def __init__(self, db: DBSessionDep):
    self.db = db

  def getRoleById(self, id: int) -> Role:
    role = self.db.get(Role,id)

    if not role:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    
    return role

  def add(self, role: Role) -> Role:
    existRole = self.db.exec(select(Role).filter_by(name=role.name)).first()

    if existRole:
      raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Role already exist by this name!")
    
    self.db.add(role)
    self.db.commit()
    self.db.refresh(role)

    return role



  