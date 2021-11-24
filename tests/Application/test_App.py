from unittest.mock import patch, MagicMock
from src.Application.App import App
from src.Services.ApiService import ApiService


@patch('src.Services.ApiService.ApiService')
def test_app_run_fine(api_service_mock: ApiService):
    api_service_instance = MagicMock()
    api_service_instance.run = MagicMock(return_value=True)
    api_service_mock.return_value = api_service_instance

    app = App(api_service_instance)
    assert 0 == app.run()


@patch('src.Services.ApiService.ApiService')
def test_app_run_error(api_service_mock: ApiService):
    api_service_instance = MagicMock()
    api_service_instance.run = MagicMock(return_value=False)
    api_service_mock.return_value = api_service_instance

    app = App(api_service_instance)
    assert -1 == app.run()
