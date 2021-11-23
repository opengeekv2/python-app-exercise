from src.Application.App import App
from src.Application.AppBuilder import AppBuilder


def test_app_builder():
    app_builder = AppBuilder()
    app = app_builder.build()
    assert type(app) == App
