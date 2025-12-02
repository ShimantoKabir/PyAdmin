from dataclasses import dataclass

@dataclass
class ProjectCreateResponseDto:
  id: int
  name: str
  orgId: int