from datetime import datetime, timezone
import random
from config import Config
from src.user.model.User import User
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto
from src.user.repository.UserRepository import UserRepository
from passlib.context import CryptContext
from fastapi import status, HTTPException
from src.user.dtos.UserResponseDto import UserResponseDto
from src.user.dtos.UserVerificationRequestDto import UserVerificationRequestDto
from src.user.dtos.UserVerificationResponseDto import UserVerificationResponseDto
from src.email.EmailService import EmailService
from src.user.dtos.ForgotPasswordOtpRequestDto import ForgotPasswordOtpRequestDto
from src.user.dtos.ForgotPasswordOtpResponseDto import ForgotPasswordOtpResponseDto
from src.org.model.Organization import Organization

class UserService:
  otpPopulationDigits: str = "0123456789"
  userCreationResMsg: str = "A otp has been sent to your mail, please use the otp and verify your account!"
  otpExpiryDuration: int = int(Config.getValByKey("OTP_EXPIRY_DURATION"))

  def __init__(
      self, 
      userRepository : UserRepository, 
      crypto: CryptContext,
      emailService : EmailService
    ):
    self.repo = userRepository
    self.crypto = crypto
    self.emailService = emailService

  def createUser(self, reqDto : UserCreateRequestDto) -> UserCreateResponseDto:
    otp = self.generateOtp()
    

    newUser = self.repo.add(User(
      email=reqDto.email,
      password=self.crypto.hash(reqDto.password),
      otp=otp,
      super=True,
      orgs=[]
    ))
    self.emailService.sendAccountVerificationOtp(newUser.email, otp)
    resUser = UserCreateResponseDto(id=newUser.id,email=newUser.email,message=self.userCreationResMsg)
    return resUser
  
  def getUserById(self, id: int)-> UserResponseDto:
    dbUser = self.repo.getUserById(id=id)
    return UserResponseDto(id=dbUser.id, email=dbUser.email)
  
  def generateOtp(self)->str:
    otp = ''.join(random.choices(self.otpPopulationDigits, k=6))
    return otp
  
  def verify(self, reqDto: UserVerificationRequestDto)-> UserVerificationResponseDto:

    dbUser: User = self.repo.getUserByEmail(reqDto.email)

    if not dbUser:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found by this email!")
    
    if dbUser.verified:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already verified!")
    
    if not dbUser.createdAt:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No otp creation date found to calculate otp expiration!")

    otpDuration: int = self.calculateSecondDiff(datetime.now(timezone.utc), dbUser.createdAt)

    if otpDuration > self.otpExpiryDuration :
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Otp expired!")

    if dbUser.otp != reqDto.otp:
      raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Otp didn't match!")
    
    dbUser.verified = True

    self.repo.updateUser(dbUser)

    resDto = UserVerificationResponseDto(message="User verified successfully!")
    return resDto
  
  def sendForgotPasswordOtp(
      self, 
      reqDto: ForgotPasswordOtpRequestDto
    ) -> ForgotPasswordOtpResponseDto :
    
    dbUser: User = self.repo.getUserByEmail(reqDto.email)

    if not dbUser:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found by this email!")
    
    otp = self.generateOtp()
    dbUser.otp = otp
    self.repo.updateUser(dbUser)

    self.emailService.sendForgotPasswordOtp(dbUser.email, otp)

    return ForgotPasswordOtpResponseDto(message="To reset your password, a otp has been sent to your mail!")
  
  def calculateSecondDiff(self, end: datetime, start: datetime) -> int:
    timeDiff = end - start
    return timeDiff.seconds