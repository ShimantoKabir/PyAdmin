from fastapi import APIRouter, Request
from src.org.dtos.OrgAddResDto import OrgAddResDto
from src.org.dtos.OrgAddReqDto import OrgAddReqDto
from src.user.dtos.UserResponseDto import UserResponseDto
from di import UserServiceDep
from fastapi import status, HTTPException

routes = APIRouter()

@routes.get("/users/{id}", tags=["user"], name="act-get-user-by-id")
async def getById(id: int, userService: UserServiceDep)-> UserResponseDto:
  return userService.getUserById(id)

@routes.post(
  "/users/organizations", 
  tags=["user"], 
  name="act-add-organization", 
  response_model=OrgAddResDto
)
async def add(
  reqDto: OrgAddReqDto, 
  userService: UserServiceDep, 
  request: Request
)-> OrgAddResDto:
  authEmail = request.headers.get("email")

  if not authEmail:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No mail found on header!")

  return userService.addOrg(reqDto, authEmail)