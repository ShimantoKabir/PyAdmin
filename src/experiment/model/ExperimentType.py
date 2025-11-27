from enum import StrEnum

class ExperimentType(StrEnum):
  AB_TEST = "AB Test"
  PERSONALIZATION = "Personalization"
  SPLIT_URL = "Split URL"
  REDIRECT = "Redirect"