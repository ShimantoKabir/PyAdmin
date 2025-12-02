from enum import StrEnum

class PermissionType(StrEnum):
  OWNER = "Owner"
  EDITOR = "Editor"
  VIEWER = "Viewer"