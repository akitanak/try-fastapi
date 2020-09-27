from datetime import date, datetime
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from try_fastapi.applications.tasks import TaskService
from try_fastapi.domains.entities.tasks import Task, Priority
from try_fastapi.modules import task_service

app = FastAPI()


app_service: TaskService = task_service


class AddTaskReq(BaseModel):
    task_name: str
    due_date: Optional[date]
    priority: Optional[Priority]


class TaskRes(BaseModel):
    id: str
    task_name: str
    due_date: Optional[date]
    priority: Optional[Priority]
    is_done: bool
    created_at: Optional[datetime]

    @classmethod
    def to_response(cls, task: Task):
        return TaskRes(
            id=str(task.id),
            task_name=task.task_name,
            due_date=task.due_date,
            priority=task.priority.value if task.priority is not None else None,
            is_done=task.is_done,
            created_at=task.created_at,
        )


@app.get("/healthz")
def healthz():
    return {"status": "I'm Healthy!"}


@app.post("/tasks/", response_model=TaskRes)
def add(add_req: AddTaskReq) -> TaskRes:
    task = app_service.add(add_req.dict())
    return TaskRes.to_response(task)


@app.get("/tasks/")
def list(response_model=List[TaskRes]) -> List[TaskRes]:
    tasks = app_service.list()
    return [TaskRes.to_response(task) for task in tasks]
