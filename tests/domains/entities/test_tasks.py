from datetime import date

import pytest
from pydantic import ValidationError
from try_fastapi.domains.entities.tasks import Priority, Task


def test_create_task_with_minimum_parameter():
    task_title = "write async db access api."

    task = Task(task_name=task_title)

    assert task.id
    assert task.task_name == task_title
    assert task.due_date is None
    assert task.priority is None
    assert task.is_done is False
    assert task.created_at is not None


def test_create_task_with_all_parameter():
    task_title = "write async db access api."
    priority = Priority.HIGH
    due_date = date.today()

    task = Task(task_name=task_title, priority=priority, due_date=due_date)

    assert task.id
    assert task.task_name == task_title
    assert task.due_date == due_date
    assert task.priority == priority
    assert task.is_done is False
    assert task.created_at is not None


def test_create_task_with_too_long_task_name():
    task_title = "123456789012345678901234567890123"

    with pytest.raises(ValidationError) as e:
        Task(task_name=task_title)

    assert len(e.value.errors()) == 1
    error = e.value.errors()[0]
    assert error["loc"] == ("task_name",)
    assert error["msg"] == "length of task_name was too long."
