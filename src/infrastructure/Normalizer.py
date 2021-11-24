from abc import ABC, abstractmethod
from src.model.todo import ToDo


class Normalizer(ABC):
    @abstractmethod
    def denormalize(self, todo_dict: dict) -> ToDo:
        pass

    @abstractmethod
    def normalize(self, todo: ToDo) -> dict:
        pass
