from enum import StrEnum

class TriggerType(StrEnum):
  IMMEDIATELY = "Immediately"
  DOM_READY = "DOM Ready"
  URL_CHANGES = "URL Changes"