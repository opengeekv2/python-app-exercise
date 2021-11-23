from unittest.mock import patch, MagicMock
from src.Application.App import App
from src.Application.AppBuilder import AppBuilder


@patch('src.Application.App.App')
@patch('src.Services.ApiService.ApiService')
@patch('src.Services.ApiService.ToDoApiReader')
def test_app_builder(app_mock, api_service_mock, todo_api_reader_mock):
    app_instance = MagicMock()
    app_mock.return_value = app_instance
    api_service_instance = MagicMock()
    api_service_mock.return_value = api_service_instance
    todo_api_reader_instance = MagicMock()
    todo_api_reader_mock.return_value = todo_api_reader_instance

    app_builder = AppBuilder()
    app = app_builder.build()
    assert type(app) == App
