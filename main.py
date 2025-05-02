from fastapi import Depends, FastAPI, Header
from src.user import UserRouter
from src.user import UserInsecureRouter
from src.menu import MenuRouter
from src.auth import AuthRouter
from src.auth.AuthMiddleware import AuthMiddleware
from fastapi.security import HTTPBearer
from typing import Annotated

def getEmail(email: Annotated[str, Header()]):
    return email

app = FastAPI()

app.include_router(UserRouter.routes, dependencies=[Depends(getEmail), Depends(HTTPBearer())])
app.include_router(MenuRouter.routes, dependencies=[Depends(getEmail), Depends(HTTPBearer())])
app.include_router(AuthRouter.routes)
app.include_router(UserInsecureRouter.routes)

app.add_middleware(AuthMiddleware)

@app.get("/",tags=["health"])
async def test()->str:
  for route in app.routes:
    print(route)
  return "App is running.....!"

