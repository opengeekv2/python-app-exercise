from sys import stderr
from abc import ABC, abstractmethod
from typing import Iterable


class ListEndpointReader(ABC):
    @abstractmethod
    def read_endpoint(self) -> Iterable:
        pass


class CsvObjectWriter(ABC):
    @abstractmethod
    def write_object(self, obj: object) -> bool:
        pass


class ApiService:
    def __init__(
        self,
        todo_api_reader: ListEndpointReader,
        todo_writer: CsvObjectWriter
    ):
        self._todo_api_reader: ListEndpointReader = todo_api_reader
        self._todo_writer: CsvObjectWriter = todo_writer

    def run(self):
        print('Running ApiService', file=stderr)
        for todo in self._todo_api_reader.read_endpoint():
            self._todo_writer.write_object(todo)
