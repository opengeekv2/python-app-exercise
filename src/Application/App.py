from src.Services.ApiService import ApiService


class App:
    def __init__(self, api_service: ApiService):
        self._api_service = api_service

    def run(self) -> int:
        try:
            result = self._api_service.run()
            if result == True:
                print("Success")
                return 0
            print("Fail")
            return -1
        except BaseException:
            print("Fail")
            return -1
