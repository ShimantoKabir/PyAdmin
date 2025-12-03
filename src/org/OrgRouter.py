from fastapi import APIRouter
from src.org.dtos.OrgAddReqDto import OrgAddReqDto
from src.org.dtos.OrgAddResDto import OrgAddResDto
from di import OrgServiceDep

routes = APIRouter()

@routes.post(
  "/organizations", 
  response_model=OrgAddResDto, 
  tags=["organization"],
  name="act:create-organization"
)
async def createOrganization(
    reqDto: OrgAddReqDto,
    orgService: OrgServiceDep
  ) -> OrgAddResDto:
  return orgService.createOrg(reqDto)