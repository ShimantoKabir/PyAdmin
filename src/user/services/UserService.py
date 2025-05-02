from src.user.model.User import User
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto
from src.user.repository.UserRepository import UserRepository
from passlib.context import CryptContext
from src.user.dtos.UserResponseDto import UserResponseDto

class UserService:
  def __init__(self, userRepository : UserRepository, crypto: CryptContext):
    self.repo = userRepository
    self.crypto = crypto

  def createUser(self, reqDto : UserCreateRequestDto) -> UserCreateResponseDto:    
    newUser = self.repo.add(User(email=reqDto.email,password=self.crypto.hash(reqDto.password)))
    resUser = UserCreateResponseDto(id=newUser.id,email=newUser.email)
    return resUser
  
  def getUserById(self, id: int)-> UserResponseDto:
    dbUser = self.repo.getUserById(id=id)
    return UserResponseDto(id=dbUser.id, email=dbUser.email)