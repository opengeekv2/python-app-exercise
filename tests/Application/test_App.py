from src.Application.App import App
from src.Services.ApiService import ApiService


def test_app_run():
    app = App(ApiService())
    assert 0 == app.run()
