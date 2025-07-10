from dataclasses import dataclass

@dataclass
class UpdateUserResponseDto:
  id: int
  disabled: bool|None
  super: bool|None
  firstName: str
  lastName: str
  contactNumber: str