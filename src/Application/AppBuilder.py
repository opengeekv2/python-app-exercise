from src.Services.ApiService import ApiService
from .App import App


class AppBuilder:

    def build(self):
        return App(ApiService())
