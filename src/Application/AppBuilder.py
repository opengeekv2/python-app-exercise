from src.Services.ApiService import ApiService
from src.infrastructure.ToDoApiReader import RequestsToDoApiReader
from .App import App


class AppBuilder:

    def build(self):
        return App(ApiService(RequestsToDoApiReader()))
