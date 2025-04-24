from src.user.model.User import User
from src.user.dtos.UserCreateRequestDto import UserCreateRequestDto
from src.user.dtos.UserCreateResponseDto import UserCreateResponseDto
from src.user.repository.UserRepository import UserRepository

class UserService:
  def __init__(self, userRepository : UserRepository):
    self.repo = userRepository

  def createUser(self, reqDto : UserCreateRequestDto) -> UserCreateResponseDto:    
    newUser = self.repo.add(User(email=reqDto.email))
    resUser = UserCreateResponseDto(id=newUser.id,email=newUser.email)
    return resUser