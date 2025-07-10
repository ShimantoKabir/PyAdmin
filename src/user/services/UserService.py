import random
from config import Config
from src.user.model.User import User
from datetime import datetime, timezone
from passlib.context import CryptContext
from fastapi import status, HTTPException
from src.org.dtos.OrgAddReqDto import OrgAddReqDto
from src.org.dtos.OrgAddResDto import OrgAddResDto
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto
from src.user.repository.UserRepository import UserRepository
from src.user.dtos.UserResponseDto import UserResponseDto
from src.user.dtos.UserVerificationRequestDto import UserVerificationRequestDto
from src.user.dtos.UserVerificationResponseDto import UserVerificationResponseDto
from src.email.EmailService import EmailService
from src.user.dtos.ForgotPasswordOtpRequestDto import ForgotPasswordOtpRequestDto
from src.user.dtos.ForgotPasswordOtpResponseDto import ForgotPasswordOtpResponseDto
from src.org.model.Organization import Organization
from src.org.repository.OrgRepository import OrgRepository
from src.user.dtos.UpdateUserRequestDto import UpdateUserRequestDto
from src.user.dtos.UpdateUserResponseDto import UpdateUserResponseDto
from src.db.repository.UserOrgLinkRepository import UserOrgLinkRepository
from src.db.links.UserOrgLink import UserOrgLink

class UserService:
  otpPopulationDigits: str = "0123456789"
  userCreationResMsg: str = "A otp has been sent to your mail, please use the otp and verify your account!"
  otpExpiryDuration: int = int(Config.getValByKey("OTP_EXPIRY_DURATION"))

  def __init__(
      self, 
      userRepository : UserRepository, 
      orgRepository: OrgRepository,
      userOrgLinkRepo: UserOrgLinkRepository,
      crypto: CryptContext,
      emailService : EmailService
    ):
    self.repo = userRepository
    self.crypto = crypto
    self.emailService = emailService
    self.orgRepo = orgRepository
    self.userOrgLinkRepo = userOrgLinkRepo

  def createUser(self, reqDto : UserCreateRequestDto) -> UserCreateResponseDto:
    otp = self.generateOtp()
    
    newUser = self.repo.add(User(
      email=reqDto.email,
      password=self.crypto.hash(reqDto.password),
      otp=otp,
      orgs=[Organization(
        name="",
        domain="",
        websites=[]
      )],
      menuTemplates=[]
    ))

    self.emailService.sendAccountVerificationOtp(newUser.email, otp)

    org: Organization|None = newUser.orgs[0] if newUser.orgs[0] else None

    if org is not None:
      userOrgLink: UserOrgLink = self.userOrgLinkRepo.get(userId=newUser.id,orgId=org.id)
      userOrgLink.disabled = False
      userOrgLink.super = True
      updatedUserOrgLink = self.userOrgLinkRepo.edit(userOrgLink=userOrgLink)

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

  def addOrg(self, reqDto: OrgAddReqDto, authMail: str) -> OrgAddResDto: 
    dbUser: User = self.repo.getUserByEmail(authMail)

    if not dbUser:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found by this email!")

    isDomainExist = any(org.domain == reqDto.domain for org in dbUser.orgs)

    if isDomainExist:
      raise HTTPException(status_code=status.HTTP_302_FOUND, detail="This organization already added for this user!")
    
    org = self.orgRepo.getUserByDomain(reqDto.domain)

    if not org:
      org = self.orgRepo.add(Organization(name=reqDto.name,domain=reqDto.domain,websites=list(map(str, reqDto.websites))))

    dbUser.orgs.append(org)
    self.repo.updateUser(dbUser)

    return OrgAddResDto(id=org.id,name=org.name,domain=org.domain,websites=org.websites)

  def updateUser(self, userId: int, orgId: int, reqDto: UpdateUserRequestDto)-> UpdateUserResponseDto:
    dbUser: User = self.repo.getUserById(userId)

    if not dbUser:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found by this ID!")
    
    if reqDto.firstName:
      dbUser.firstName = reqDto.firstName

    if reqDto.lastName:
     dbUser.lastName = reqDto.lastName

    if reqDto.contactNumber:
      dbUser.contactNumber = reqDto.contactNumber

    updateUser = self.repo.updateUser(dbUser)

    userOrgLink: UserOrgLink|None = self.userOrgLinkRepo.get(userId=userId,orgId=orgId)

    if userOrgLink is not None:
      if reqDto.disabled is not None:
        userOrgLink.disabled = reqDto.disabled

      if reqDto.super is not None:
        userOrgLink.super = reqDto.super

      self.userOrgLinkRepo.edit(userOrgLink=userOrgLink)

    return UpdateUserResponseDto(
      id=updateUser.id, 
      disabled= None if userOrgLink is None else userOrgLink.disabled,
      super= None if userOrgLink is None else userOrgLink.super,
      firstName=updateUser.firstName,
      lastName=updateUser.lastName,
      contactNumber=updateUser.contactNumber
    )






    
    