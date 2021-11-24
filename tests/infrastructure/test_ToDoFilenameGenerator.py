from datetime import date
from src.model.todo import ToDo
from src.infrastructure.ToDoFilenameGenerator import ToDoFilenameGenerator


def test_todo_filename_generator():
    today = date.today()
    todo = ToDo(1, 1, 'hola', False)
    file_generator = ToDoFilenameGenerator()
    filename = file_generator.generate_filename(todo, today)
    assert str(today.year) + '_' + str(today.month) + '_' + \
        str(today.day) + '_' + str(todo.id) == filename
