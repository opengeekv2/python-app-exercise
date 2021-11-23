from src.Services.ApiService import ApiService


class App:
    def __init__(self, api_service: ApiService):
        self._api_service = api_service

    def run(self) -> int:
        self._api_service.run()
        return 0
