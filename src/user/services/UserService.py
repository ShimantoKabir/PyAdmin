from fastapi import HTTPException, status
from sqlmodel import select
from db import DBSessionDep
from models import User
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto

class UserService:
  def createUser(
    self,
    dto : UserCreateRequestDto,
    db: DBSessionDep
  ) -> UserCreateResponseDto:

    existUser = db.exec(select(User).filter_by(email=dto.email)).first()

    if existUser:
      raise HTTPException(status_code=status.HTTP_302_FOUND, detail="User already exist by this mail!")
      

    user = User()
    user.email = dto.email

    db.add(user)
    db.commit()
    db.refresh(user)

    ucr = UserCreateResponseDto(id=user.id, email=user.email)
    return ucr