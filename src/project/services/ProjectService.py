from src.project.repository.ProjectRepository import ProjectRepository
from src.db.repository.UserProjectLinkRepository import UserProjectLinkRepository
from src.project.dtos.ProjectCreateRequestDto import ProjectCreateRequestDto
from src.project.dtos.ProjectCreateResponseDto import ProjectCreateResponseDto
from src.project.dtos.ProjectResponseDto import ProjectResponseDto
from src.project.model.Project import Project
from src.db.links.UserProjectLink import UserProjectLink
from src.utils.pagination.PaginationRequestDto import PaginationRequestDto
from src.utils.pagination.PaginationResponseDto import PaginationResponseDto
from src.db.links.PermissionType import PermissionType

class ProjectService:
  def __init__(
      self, 
      projectRepo: ProjectRepository, 
      linkRepo: UserProjectLinkRepository
    ):
    self.repo = projectRepo
    self.linkRepo = linkRepo

  def createProject(self, reqDto: ProjectCreateRequestDto, userId: int) -> ProjectCreateResponseDto:
    # 1. Create the project
    newProject = self.repo.add(Project(
      name=reqDto.name,
      description=reqDto.description,
      orgId=reqDto.orgId
    ))

    # 2. Link the creating user as a Super Admin for this project
    self.linkRepo.add(UserProjectLink(
      userId=userId,
      projectId=newProject.id,
      super=True,
      disabled=False,
      permissionType=PermissionType.OWNER
    ))

    return ProjectCreateResponseDto(
      id=newProject.id,
      name=newProject.name,
      orgId=newProject.orgId
    )

  def getProjects(self, reqDto: PaginationRequestDto) -> PaginationResponseDto[ProjectResponseDto]:
    total: int | None = reqDto.total
    
    if reqDto.total is None or reqDto.total == 0:
      total = self.repo.countAllProjects(orgId=reqDto.orgId)

    projects: list[Project] = self.repo.getAllProjects(
      rows=reqDto.rows, 
      page=reqDto.page, 
      orgId=reqDto.orgId
    )

    items: list[ProjectResponseDto] = []
    for p in projects:
      items.append(ProjectResponseDto(
        id=p.id,
        name=p.name,
        description=p.description,
        orgId=p.orgId,
        orgName=p.org.name if p.org else ""
      ))

    return PaginationResponseDto[ProjectResponseDto](items=items, total=total)