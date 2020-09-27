from typing import Dict, List

from try_fastapi.domains.entities.tasks import Priority, Task


class TaskService:
    def add(self, task_dict: Dict) -> Task:
        task = Task(
            task_name=task_dict["task_name"],
            due_date=task_dict.get("due_date"),
            priority=task_dict.get("priority"),
        )
        return task

    def list(self) -> List[Task]:
        return [to_task(task) for task in tasks]


tasks = [
    {"task_name": "歯を磨く"},
    {"task_name": "顔を洗う", "priority": "high"},
    {"task_name": "朝ごはんを食べる", "priority": "low"},
]


def to_task(task_dict: Dict) -> Task:
    return Task(
        task_name=task_dict["task_name"],
        due_date=task_dict.get("due_date"),
        priority=Priority.valueOf(task_dict.get("priority"))
        if task_dict.get("priority") is not None
        else None,
    )
