from unittest.mock import patch, mock_open, MagicMock
from datetime import date
from src.infrastructure.ObjectWriter import CsvFileWriter
from src.model.todo import ToDo
import csv
import os


@patch('src.infrastructure.ToDoNormalizer.ToDoNormalizer')
@patch('src.infrastructure.ToDoFilenameGenerator.ToDoFilenameGenerator')
def test_todo_writer(todo_normalizer_mock, todo_filename_mock):
    filename = 'filename'

    todo = ToDo(1, 1, 'Hola', False)
    todo_dict = {
        'userId': 1,
        'id': 1,
        'title': 'Hola',
        'completed': False
    }

    todo_normalizer_instance = MagicMock()
    todo_normalizer_instance.normalize = MagicMock(return_value=todo_dict)
    todo_normalizer_mock.return_value = todo_normalizer_instance

    todo_filename_instance = MagicMock()
    todo_filename_instance.generate_filename = MagicMock(
        return_value='filename')
    todo_filename_mock.return_value = todo_filename_instance

    today = date.today()
    todo_writer = CsvFileWriter(
        todo_normalizer_instance,
        todo_filename_instance,
        os.getenv('STORAGE_FOLDER'),
    )
    todo_writer.write_object(todo, today)
    with open(os.getenv('STORAGE_FOLDER') + '/' + filename + '.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            assert int(row['userId']) == todo_dict['userId']
            assert int(row['id']) == todo_dict['id']
            assert row['title'] == todo_dict['title']
            assert ('True' == row['completed']) == todo_dict['completed']
    os.remove(os.getenv('STORAGE_FOLDER') + '/' + filename + '.csv')
