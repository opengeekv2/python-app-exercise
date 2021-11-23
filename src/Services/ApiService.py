from sys import stderr
from abc import ABC, abstractmethod


class ToDoApiReader(ABC):
    @abstractmethod
    def read_api(self):
        pass


class ApiService:
    def __init__(self, todo_api_reader: ToDoApiReader):
        self._todo_api_reader: ToDoApiReader = todo_api_reader

    def run(self):
        print('Running ApiService', file=stderr)
        todos = self._todo_api_reader.read_todos()
        # TODO: follow README.md instructions
