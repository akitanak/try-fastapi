from datetime import date, datetime
from typing import List, Optional
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel

from try_fastapi.applications.tasks import TaskService
from try_fastapi.domains.entities.tasks import Priority
from try_fastapi.modules import task_service

app = FastAPI()


app_service: TaskService = task_service


class AddTaskRequest(BaseModel):
    task_name: str
    due_date: Optional[date]
    priority: Optional[Priority]


class TaskResponse(BaseModel):
    id: UUID
    task_name: str
    due_date: Optional[date]
    priority: Optional[Priority]
    is_done: bool
    created_at: datetime

    class Config:
        orm_mode = True


@app.get("/healthz")
def healthz():
    return {"status": "I'm Healthy!"}


@app.post("/tasks/", response_model=TaskResponse)
def add(add_req: AddTaskRequest) -> TaskResponse:
    task = app_service.add(add_req.dict())
    return TaskResponse.from_orm(task)


@app.get("/tasks/", response_model=List[TaskResponse])
def list() -> List[TaskResponse]:
    tasks = app_service.list()
    return [TaskResponse.from_orm(task) for task in tasks]
