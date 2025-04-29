from src.auth.repository.AuthRepository import AuthRepository
from di import DBSessionDep
from src.user.model.User import User
from sqlmodel import select

class AuthRepositoryImp(AuthRepository):

  def __init__(self, db: DBSessionDep):
    self.db = db

  def getUserByEmail(self, email: str) -> User:
    return self.db.exec(select(User).filter_by(email=email)).first()