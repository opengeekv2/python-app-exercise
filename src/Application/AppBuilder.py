from src.Services.ApiService import ApiService
from src.infrastructure.ListEndpointReader import RequestsChunkedListEndpointReader
from src.infrastructure.ToDoNormalizer import ToDoNormalizer
from src.infrastructure.ToDoFilenameGenerator import ToDoFilenameGenerator
from src.infrastructure.ObjectWriter import CsvFileWriter
from .App import App
from dotenv import load_dotenv
import os


class AppBuilder:

    def build(self):
        load_dotenv()
        return App(
            ApiService(
                RequestsChunkedListEndpointReader(
                    os.getenv('API_ROOT') + '/todos/',
                    ToDoNormalizer()
                ),
                CsvFileWriter(
                    ToDoNormalizer(),
                    ToDoFilenameGenerator(),
                    os.getenv('STORAGE_FOLDER', './storage'))
            )
        )
