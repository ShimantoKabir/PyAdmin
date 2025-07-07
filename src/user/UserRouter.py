from fastapi import APIRouter, Request
from src.org.dtos.OrgAddResDto import OrgAddResDto
from src.org.dtos.OrgAddReqDto import OrgAddReqDto
from src.user.dtos.UserResponseDto import UserResponseDto
from di import UserServiceDep
from fastapi import status, HTTPException
from src.user.dtos.UpdateUserRequestDto import UpdateUserRequestDto
from src.user.dtos.UpdateUserResponseDto import UpdateUserResponseDto

routes = APIRouter()

@routes.get("/users/{id}", tags=["user"], name="act:get-user-by-id")
async def getById(id: int, userService: UserServiceDep)-> UserResponseDto:
  return userService.getUserById(id)

@routes.patch(
  "/users/{id}", 
  tags=["user"],
  name="act:update-user-by-id",
  response_model=UpdateUserResponseDto
)
async def updateById(
  id: int, 
  reqDto: UpdateUserRequestDto, 
  userService: UserServiceDep
)-> UserResponseDto:
  return userService.updateUserById(id, reqDto)

@routes.post(
  "/users/organizations", 
  tags=["user"], 
  name="act:add-organization", 
  response_model=OrgAddResDto
)
async def addOrg(
  reqDto: OrgAddReqDto, 
  userService: UserServiceDep, 
  request: Request
)-> OrgAddResDto:
  authEmail = request.headers.get("email")

  if not authEmail:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No mail found on header!")

  return userService.addOrg(reqDto, authEmail)