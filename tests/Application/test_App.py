from unittest.mock import patch
from src.Application.App import App
from src.Services.ApiService import ApiService


@patch('src.Services.ApiService.ApiService')
def test_app_run(api_service_mock: ApiService):
    app = App(api_service_mock)
    assert 0 == app.run()
