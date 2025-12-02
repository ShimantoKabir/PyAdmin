from dataclasses import dataclass
from typing import Optional

@dataclass
class ProjectResponseDto:
  id: int
  name: str
  description: Optional[str]
  orgId: int
  orgName: str