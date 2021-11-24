
from src.model.todo import ToDo
from datetime import date
from src.infrastructure.FilenameGenerator import FilenameGenerator


class ToDoFilenameGenerator(FilenameGenerator):
    def generate_filename(self, todo: ToDo, today: date = date.today()) -> str:
        return '{}_{}_{}_{}'.format(
            today.year, today.month, today.day, todo.id)
