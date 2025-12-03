from src.role.repository.RoleRepository import RoleRepository
from src.role.model.Role import Role
from db import DBSessionDep
from fastapi import status, HTTPException
from sqlmodel import select
from sqlalchemy import func

class RoleRepositoryImp(RoleRepository):
  def __init__(self, db: DBSessionDep):
    self.db = db

  def getRoleById(self, id: int) -> Role:
    role = self.db.get(Role, id)
    if not role:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return role

  def add(self, role: Role) -> Role:
    # Change 1: Check uniqueness based on Name AND OrgId
    existRole = self.db.exec(
        select(Role)
        .where(Role.name == role.name)
        .where(Role.orgId == role.orgId)
    ).first()

    if existRole:
      # Option A: Return existing (Idempotent)
      return existRole
      # Option B: Raise Error (Strict)
      # raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Role already exists!")
    
    self.db.add(role)
    self.db.commit()
    self.db.refresh(role)
    return role
  
  def getAllRole(self, rows: int, page: int, orgId: int) -> list[Role]:
    offset: int = (page - 1) * rows
    # Change 2: Simplified query. No join needed.
    return self.db.exec(
      select(Role)
      .where(Role.orgId == orgId)
      .offset(offset).limit(rows)
    ).all()
  
  def countAllRole(self, orgId: int) -> int:
    # Change 3: Simplified count query.
    return self.db.exec(
      select(func.count(Role.id))
      .where(Role.orgId == orgId)
    ).one()