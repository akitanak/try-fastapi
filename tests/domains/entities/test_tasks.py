from datetime import date
from try_fastapi.domains.entities.tasks import Task, Priority


def test_create_task_with_minimum_parameter():
    task_title = "write async db access api with FastAPI."

    task = Task(task_name=task_title)

    assert task.id
    assert task.task_name == task_title
    assert task.due_date is None
    assert task.priority is None
    assert task.is_done is False
    assert task.created_at is not None


def test_create_task_with_all_parameter():
    task_title = "write async db access api with FastAPI."
    priority = Priority.HIGH
    due_date = date.today()

    task = Task(task_name=task_title, priority=priority, due_date=due_date)

    assert task.id
    assert task.task_name == task_title
    assert task.due_date == due_date
    assert task.priority == priority
    assert task.is_done is False
    assert task.created_at is not None
