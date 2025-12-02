from fastapi import APIRouter, Request, status, HTTPException
from di import ProjectServiceDep, UserServiceDep
from src.project.dtos.ProjectCreateRequestDto import ProjectCreateRequestDto
from src.project.dtos.ProjectCreateResponseDto import ProjectCreateResponseDto
from src.project.dtos.ProjectResponseDto import ProjectResponseDto
from src.utils.pagination.PaginationRequestDto import PaginationRequestDto
from src.utils.pagination.PaginationResponseDto import PaginationResponseDto

routes = APIRouter()

@routes.post(
  "/projects/", 
  response_model=ProjectCreateResponseDto, 
  tags=["project"],
  name="act:create-project"
)
async def createProject(
    reqDto: ProjectCreateRequestDto,
    projectService: ProjectServiceDep,
    userService: UserServiceDep,
    request: Request
  ) -> ProjectCreateResponseDto:
  
  # Extract email from header (set by AuthMiddleware)
  email = request.headers.get("email")
  if not email:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User email not found")
      
  # We need the User ID to link them to the project
  user = userService.repo.getUserByEmail(email)
  if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

  return projectService.createProject(reqDto, user.id)

@routes.post(
  "/projects/all",
  tags=["project"],
  name="act:get-projects",
  response_model=PaginationResponseDto[ProjectResponseDto]
)
async def getProjects(
  reqDto: PaginationRequestDto, 
  projectService: ProjectServiceDep
) -> PaginationResponseDto[ProjectResponseDto]:  
  return projectService.getProjects(reqDto)