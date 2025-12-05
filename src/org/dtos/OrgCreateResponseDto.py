from dataclasses import dataclass

@dataclass
class OrgCreateResponseDto:
  id: int
  name: str 
  email: str