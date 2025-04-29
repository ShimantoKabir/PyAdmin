from passlib.context import CryptContext
from src.auth.repository.AuthRepository import AuthRepository
from src.auth.dtos.LoginRequestDto import LoginRequestDto
from src.auth.dtos.LoginResponseDto import LoginResponseDto
from src.user.model.User import User
from fastapi import status, HTTPException
import jwt
from datetime import datetime, timedelta, timezone
from config import Config

class AuthService:
  def __init__(self, authRepository : AuthRepository, crypto: CryptContext):
    self.repo = authRepository
    self.crypto = crypto

  def login(self, reqDto: LoginRequestDto) -> str:
    dbUser: User = self.repo.getUserByEmail(reqDto.email)

    if not dbUser:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user fund by this email!")
  
    isPasswordVerified = self.crypto.verify(reqDto.password, dbUser.password)

    if not isPasswordVerified:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password!")
    
    accessTokenExpires = datetime.now(timezone.utc) + timedelta(int(Config.getValByKey("ACCESS_TOKEN_EXPIRE_MINUTES")))
    refreshTokenExpires = datetime.now(timezone.utc) + timedelta(int(Config.getValByKey("REFRESH_TOKEN_EXPIRE_MINUTES")))

    print("accessTokenExpires",accessTokenExpires)

    accessToken = jwt.encode({
      "sub" : dbUser.email,
      "exp" : accessTokenExpires
    },Config.getValByKey("SECRET_KEY"), Config.getValByKey("ALGORITHM"))

    refreshToken = jwt.encode({
      "sub" : dbUser.email,
      "exp" : refreshTokenExpires
    },Config.getValByKey("SECRET_KEY"), Config.getValByKey("ALGORITHM"))

    res = LoginResponseDto(accessToken=accessToken, refreshToken=refreshToken)
    return res
  
