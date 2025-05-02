from passlib.context import CryptContext
from src.auth.repository.AuthRepository import AuthRepository
from src.auth.dtos.LoginRequestDto import LoginRequestDto
from src.auth.dtos.LoginResponseDto import LoginResponseDto
from src.user.model.User import User
from fastapi import status, HTTPException
import jwt
from datetime import datetime, timedelta, timezone
from config import Config
from src.auth.dtos.AuthRefreshResponseDto import AuthRefreshResponseDto
from src.auth.dtos.AuthRefreshRequestDto import AuthRefreshRequestDto
from jwt import ExpiredSignatureError
from src.auth.dtos.tokens import Token

class AuthService:
  def __init__(self, authRepository : AuthRepository, crypto: CryptContext):
    self.repo = authRepository
    self.crypto = crypto

  def login(self, reqDto: LoginRequestDto) -> str:
    dbUser: User = self.repo.getUserByEmail(reqDto.email)

    if not dbUser:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found by this email!")
  
    isPasswordVerified = self.crypto.verify(reqDto.password, dbUser.password)

    if not isPasswordVerified:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password!")
    
    token = self.generateToken(dbUser.email)

    res = LoginResponseDto(accessToken=token.accessToken, refreshToken=token.refreshToken)
    return res
  
  def refresh(self, authRefreshRequestDto: AuthRefreshRequestDto)-> AuthRefreshResponseDto:
    refreshToken = authRefreshRequestDto.refreshToken

    try:
      payload = jwt.decode(refreshToken, Config.getValByKey("SECRET_KEY"), Config.getValByKey("ALGORITHM"))
    except ExpiredSignatureError as e:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired!")

    payloadEmail = payload.get("sub")

    if payloadEmail is None:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No email found on token payload!")
    
    dbUser: User = self.repo.getUserByEmail(payloadEmail)

    if not dbUser:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found by this email!")
    
    token = self.generateToken(dbUser.email)

    res  = AuthRefreshResponseDto(accessToken=token.accessToken,refreshToken=token.refreshToken)
    return res
  
  def generateToken(self, email: str)->Token:
    accessTokenExpires = datetime.now(timezone.utc) + timedelta(minutes=int(Config.getValByKey("ACCESS_TOKEN_EXPIRE_MINUTES")))
    refreshTokenExpires = datetime.now(timezone.utc) + timedelta(minutes=int(Config.getValByKey("REFRESH_TOKEN_EXPIRE_MINUTES")))

    accessToken = jwt.encode({
      "sub" : email,
      "exp" : accessTokenExpires
    }, Config.getValByKey("SECRET_KEY"), Config.getValByKey("ALGORITHM"))

    refreshToken = jwt.encode({
      "sub" : email,
      "exp" : refreshTokenExpires
    }, Config.getValByKey("SECRET_KEY"), Config.getValByKey("ALGORITHM"))
    
    return Token(accessToken=accessToken,refreshToken=refreshToken)

  
