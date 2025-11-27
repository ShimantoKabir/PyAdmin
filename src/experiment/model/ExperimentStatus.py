from enum import StrEnum

class ExperimentStatus(StrEnum):
  DRAFT = "Draft"
  ACTIVE = "Active"
  PAUSED = "Paused"
  ARCHIVED = "Archived"
  ENDED = "Ended"