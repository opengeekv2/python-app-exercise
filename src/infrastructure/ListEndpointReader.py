import io
import json
from typing import Generator
import requests
from requests import Response
from src.Services.ApiService import ListEndpointReader
from src.infrastructure.Normalizer import Normalizer


class RequestsChunkedListEndpointReader(ListEndpointReader):
    def __init__(self, endpoint: str, normalizer: Normalizer):
        self._endpoint = endpoint
        self._normalizer = normalizer

    def read_endpoint(self) -> Generator:
        try:
            with requests.get(self._endpoint, stream=True) as s:
                json_chunk = b''
                for line in s.iter_lines():
                    if line in [b'[', b']']:
                        continue
                    if line == b'  {':
                        json_chunk = b'{'
                        continue
                    if line in [b'  },', b'  }']:
                        json_chunk += b'}'
                        yield json.load(io.BytesIO(json_chunk), object_hook=self._normalizer.denormalize)
                    json_chunk += line
        except Exception as ex:
            print('Error connecting or parsing endpoint content.')
            print('You may change the endpoint setting the API_ROOT environment variable or setting it up in the .env file.')
        return
