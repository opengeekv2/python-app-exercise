import contextlib
from unittest.mock import patch, MagicMock
from src.Services.ApiService import ApiService, ToDoApiReader
from src.infrastructure.ToDoApiReader import RequestsToDoApiReader


@patch('src.infrastructure.ToDoApiReader.RequestsToDoApiReader')
def test_calls_read_todos(capsys):
    api_reader: ToDoApiReader = RequestsToDoApiReader()
    api_reader.read_todos = MagicMock(return_value=[])
    ApiService(api_reader).run()
    assert api_reader.read_todos.call_count == 1
