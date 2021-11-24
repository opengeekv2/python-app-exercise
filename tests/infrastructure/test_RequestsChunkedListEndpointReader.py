from typing import Generator
from unittest.mock import MagicMock, patch
from src.infrastructure.ListEndpointReader import RequestsChunkedListEndpointReader
from src.model.todo import ToDo


@patch('src.infrastructure.ToDoNormalizer.ToDoNormalizer')
def test_todo_api_reader_requests_does_request(todo_normalizer_mock):
    endpoint = 'https://jsonplaceholder.typicode.com/todos/'
    todo_normalizer_instance = MagicMock()
    todo_normalizer_instance.denormalize = MagicMock(
        return_value=ToDo(1, 1, "Hola", False)
    )
    todo_normalizer_mock.return_value = todo_normalizer_instance

    todo_api_reader = RequestsChunkedListEndpointReader(
        endpoint,
        todo_normalizer_instance
    )
    assert isinstance(todo_api_reader.read_endpoint(), Generator)
    assert isinstance(next(todo_api_reader.read_endpoint()), ToDo)
