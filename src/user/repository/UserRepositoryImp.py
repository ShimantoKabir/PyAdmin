from src.user.repository.UserRepository import UserRepository
from src.user.model.User import User
from db import DBSessionDep
from fastapi import status, HTTPException
from sqlmodel import select

class UserRepositoryImp(UserRepository):
  def __init__(self, db: DBSessionDep):
    self.db = db

  def getUserById(self, id: int) -> User:
    user = self.db.get(User,id)
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

  def add(self, user: User) -> User:
    existUser = self.db.exec(select(User).filter_by(email=user.email)).first()

    if existUser:
      raise HTTPException(status_code=status.HTTP_302_FOUND, detail="User already exist by this name!")
    
    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)

    return user
  
  def getUserByEmail(self, email: str) -> User:
    return self.db.exec(select(User).filter_by(email=email)).first()
  
  def updateUser(self, user: User):

    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)

    return user
  
  def getAllUser(self)->User:
    pass

  