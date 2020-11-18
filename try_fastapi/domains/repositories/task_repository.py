from abc import ABC, abstractmethod
from typing import List
from try_fastapi.domains.entities.tasks import Task


class TaskRepository(ABC):
    @abstractmethod
    async def create(self, task: Task) -> Task:
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, id: str) -> Task:
        raise NotImplementedError
