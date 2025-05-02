from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine
from config import Config

engine = create_engine(Config.getValByKey("DB_URL"),echo=True)

def get_session():
  with Session(engine) as session:
    yield session

DBSessionDep = Annotated[Session, Depends(get_session)]