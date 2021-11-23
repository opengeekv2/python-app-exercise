from src.infrastructure.ToDoApiReader import RequestsToDoApiReader


def test_todo_api_reader_requests_does_request():
    todo_api_reader = RequestsToDoApiReader()
    assert [] == todo_api_reader.read_api()
