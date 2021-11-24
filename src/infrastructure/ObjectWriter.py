from src.Services.ApiService import CsvObjectWriter
from src.infrastructure.FilenameGenerator import FilenameGenerator
from src.infrastructure.ToDoNormalizer import ToDoNormalizer
from datetime import date
from csv import DictWriter


class CsvFileWriter(CsvObjectWriter):
    def __init__(self, todo_normalizer: ToDoNormalizer,
                 filename_generator: FilenameGenerator, storage_folder: str):
        self._todo_normalizer = todo_normalizer
        self._storage_folder = storage_folder
        self._filename_generator = filename_generator

    def write_object(self, obj: object, today=None):
        if today == None:
            today = date.today()
        obj_dict = self._todo_normalizer.normalize(obj)
        try:
            with open(self._storage_folder + '/' + self._filename_generator.generate_filename(obj) + '.csv', 'w', encoding='utf-8', newline='') as csv_file:
                fieldnames = obj_dict.keys()
                writer = DictWriter(
                    csv_file, fieldnames=fieldnames, dialect='excel')
                writer.writeheader()
                writer.writerow(obj_dict)
        except BaseException:
            print("There's been a problem write files.'")
            print('Check the user running this has writing permissions.')
            print(
                'Check if the drive is mounted and accessible by the OS and that is not full.'
            )
            print(
                'The path can be adjusted setting the STORAGE_FOLDER env var or setting it in the .env file at the .'
            )
            raise
