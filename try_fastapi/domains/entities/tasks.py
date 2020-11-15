from dataclasses import dataclass, field
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
    id: UUID = field(default_factory=uuid4, init=False)
    task_name: str
    due_date: Optional[date] = field(default=None)
    priority: Optional[Priority] = field(default=None)
    is_done: bool = field(default=False, init=False)
    created_at: datetime = field(default_factory=datetime.utcnow, init=False)
