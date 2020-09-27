from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4


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


@dataclass
class Task:
    id: UUID
    task_name: str
    due_date: Optional[date]
    priority: Optional[Priority]
    is_done: bool
    created_at: datetime

    def __init__(
        self, task_name: str, due_date: Optional[date], priority: Optional[Priority]
    ):
        self.id = uuid4()
        self.task_name = task_name
        self.due_date = due_date
        self.priority = priority
        self.is_done = False
        self.created_at = datetime.utcnow()
