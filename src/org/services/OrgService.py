import random
from src.org.repository.OrgRepository import OrgRepository
from src.org.dtos.OrgAddReqDto import OrgAddReqDto
from src.org.dtos.OrgAddResDto import OrgAddResDto
from src.org.model.Organization import Organization
from src.user.repository.UserRepository import UserRepository
from src.user.model.User import User
from fastapi import HTTPException, status
from passlib.context import CryptContext
from src.utils.FileService import FileService
from src.role.repository.RoleRepository import RoleRepository
from src.role.model.Role import Role
from src.menutemplate.repository.MenuTemplateRepository import MenuTemplateRepository
from src.menutemplate.model.MenuTemplate import MenuTemplate
from src.email.EmailService import EmailService
from src.utils.Constants import OTP_POPULATION_DIGITS

class OrgService:
  def __init__(
      self, 
      orgRepo: OrgRepository, 
      userRepo: UserRepository,
      roleRepo: RoleRepository,
      crypto: CryptContext,
      fileService: FileService,
      emailService : EmailService
    ):
    self.repo = orgRepo
    self.userRepo = userRepo
    self.roleRepo = roleRepo
    self.crypto = crypto
    self.fileService = fileService
    self.emailService = emailService

  def createOrg(self, reqDto: OrgAddReqDto) -> OrgAddResDto:
    # 1. Automatic Domain Extraction
    try:
        domain = reqDto.email.split("@")[1]
    except IndexError:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format"
      )

    # 2. Validation: Ensure Org does not exist
    existingOrg = self.repo.getByDomain(domain)
    if existingOrg:
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, 
        detail="Organization already exists with this domain!"
      )
    
    # 3. Validation: Ensure User does not exist
    existingUser = self.userRepo.getUserByEmail(reqDto.email)
    if existingUser:
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="User already exists with this email!"
      )

    # 4. Create Organization
    newOrg = self.repo.add(Organization(
      name=reqDto.name,
      email=reqDto.email,
      domain=domain
    ))

    # 4. Create Role
    self.roleRepo.add(Role(name="Admin",orgId=newOrg.id))

    adminMenuTree = self.fileService.readFile("static/menu.json")
    adminMenuTemplate = MenuTemplate(
      name="Admin Menu Template",
      orgId=newOrg.id,
      tree=adminMenuTree
    )

    otp = self.generateOtp()

    # 5. Create User and Link Org
    truncatedPassword = reqDto.password[:72]
    newUser = self.userRepo.add(User(
      email=reqDto.email,
      password=self.crypto.hash(truncatedPassword),
      verified=False, 
      otp=otp,
      orgs=[newOrg],
      menuTemplates=[adminMenuTemplate]
    ))

    self.emailService.sendAccountVerificationOtp(newUser.email, otp)

    return OrgAddResDto(
      id=newOrg.id, 
      name=newOrg.name, 
      email=newOrg.email
    )
  
  def generateOtp(self)->str:
    otp = ''.join(random.choices(OTP_POPULATION_DIGITS, k=6))
    return otp