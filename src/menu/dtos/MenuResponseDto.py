from dataclasses import dataclass

@dataclass
class MenuResponseDto:
  id: int
  label: str
  icon: str
  href: str