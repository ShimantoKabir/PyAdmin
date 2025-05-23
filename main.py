from fastapi import Depends, FastAPI, Header, BackgroundTasks
from src.user import UserRouter
from src.user import UserInsecureRouter
from src.menu import MenuRouter
from src.auth import AuthRouter
from src.auth.AuthMiddleware import AuthMiddleware
from fastapi.security import HTTPBearer
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

def getEmail(email: Annotated[str, Header()]):
  return email

app = FastAPI()

app.include_router(UserRouter.routes, dependencies=[Depends(getEmail), Depends(HTTPBearer())])
app.include_router(MenuRouter.routes, dependencies=[Depends(getEmail), Depends(HTTPBearer())])
app.include_router(AuthRouter.routes)
app.include_router(UserInsecureRouter.routes)

app.add_middleware(AuthMiddleware)

origins = [
  "http://localhost:3000",  
  "http://127.0.0.1:3000",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,             
  allow_credentials=True,            
  allow_methods=["*"],               
  allow_headers=["*"],               
)

def writeLog(message: str):
  print(message)

@app.get("/",tags=["health"])
async def test()->str:
  return "App is running.....!"

