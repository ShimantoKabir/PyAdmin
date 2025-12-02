from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Text, Column, DateTime, func
from typing import Optional
from datetime import datetime

from src.experiment.model.ConditionType import ConditionType
from src.experiment.model.TriggerType import TriggerType
from src.experiment.model.ExperimentType import ExperimentType
from src.experiment.model.ExperimentStatus import ExperimentStatus

class Experiment(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  js: str = Field(default=None, nullable=True, sa_type=Text)
  css: str = Field(default=None, nullable=True, sa_type=Text)
  url: str = Field(default=None, nullable=True)
  type: ExperimentType = Field(default=ExperimentType.AB_TEST)
  title: str = Field(default=None, nullable=True)
  status: ExperimentStatus = Field(default=ExperimentStatus.DRAFT)
  metrics: list["Metrics"] = Relationship(back_populates="experiment") # type: ignore
  conditions: list["Condition"] = Relationship(back_populates="experiment") # type: ignore
  variations: list["Variation"] = Relationship(back_populates="experiment") # type: ignore
  description: str = Field(default=None, nullable=True)
  triggerType: TriggerType = Field(default=TriggerType.IMMEDIATELY)
  conditionType: ConditionType = Field(default=ConditionType.ALL)
  project: Optional["Project"] = Relationship(back_populates="experiments") # type: ignore
  projectId: Optional[int] = Field(default=None, foreign_key="project.id")
  createdAt: Optional[datetime] = Field(
    sa_column=Column(
      DateTime(timezone=True), server_default=func.now(), nullable=True
    )
  )
  updatedAt: Optional[datetime] = Field(
    sa_column=Column(
      DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
  )
  

  

