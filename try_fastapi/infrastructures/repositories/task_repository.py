from datetime import date, datetime
from typing import Optional
from uuid import UUID
from try_fastapi.domains.entities.tasks import Priority, Task
from try_fastapi.domains.repositories.task_repository import TaskRepository
from . import db


class TaskRecord(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.String(36), primary_key=True)
    task_name = db.Column(db.String(32), nullable=False)
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.String(8), nullable=True)
    is_done = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.id = str(kwargs["id"])
        self.task_name = kwargs["task_name"]
        self.due_date = kwargs.get("due_date")
        self.priority = kwargs.get("priority")
        self.is_done = kwargs["is_done"]
        self.created_at = kwargs["created_at"]
        self.updated_at = kwargs["updated_at"]


class RDBTaskRepository(TaskRepository):
    async def create(self, task: Task) -> Task:
        await TaskRecord.create(**dict(task))
        return task
