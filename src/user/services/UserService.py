from src.user.model.User import User
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto
from src.user.repository.UserRepository import UserRepository
from passlib.context import CryptContext

class UserService:
  def __init__(self, userRepository : UserRepository, crypto: CryptContext):
    self.repo = userRepository
    self.crypto = crypto

  def createUser(self, reqDto : UserCreateRequestDto) -> UserCreateResponseDto:    
    newUser = self.repo.add(User(email=reqDto.email,password=self.crypto.hash(reqDto.password)))
    resUser = UserCreateResponseDto(id=newUser.id,email=newUser.email)
    return resUser