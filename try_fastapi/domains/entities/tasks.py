from datetime import date, datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, validator


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    @classmethod
    def valueOf(cls, value: Optional[str]):
        if value is None:
            return None
        elif value.lower() == Priority.LOW.value:
            return Priority.LOW
        elif value.lower() == Priority.MEDIUM.value:
            return Priority.MEDIUM
        elif value.lower() == Priority.HIGH.value:
            return Priority.HIGH
        else:
            raise ValueError(f"Priority are low, medium, high. acutual: {value}")


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    task_name: str
    due_date: Optional[date] = Field(default=None)
    priority: Optional[Priority] = Field(default=None)
    is_done: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    @validator("task_name")
    def check_task_name_length(cls, task_name: str) -> str:
        if len(task_name) > 32:
            raise ValueError("length of task_name was too long.")
        return task_name
