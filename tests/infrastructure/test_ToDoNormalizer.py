from src.infrastructure.ToDoNormalizer import ToDoNormalizer
from src.model.todo import ToDo


def test_todo_denormalizer():
    todo_normalizer: ToDoNormalizer = ToDoNormalizer()
    todo_dict = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }
    todo = todo_normalizer.denormalize(todo_dict)
    assert isinstance(todo, ToDo)
    assert todo.userId == todo_dict['userId']
    assert todo.id == todo_dict['id']
    assert todo.title == todo_dict['title']
    assert todo.completed == todo_dict['completed']


def test_todo_denormalizer2():
    todo_normalizer: ToDoNormalizer = ToDoNormalizer()
    todo_dict = {
        "userId": 2,
        "id": 2,
        "title": "delectus aut autem",
        "completed": False
    }
    todo = todo_normalizer.denormalize(todo_dict)
    assert isinstance(todo, ToDo)
    assert todo.userId == todo_dict['userId']
    assert todo.id == todo_dict['id']
    assert todo.title == todo_dict['title']
    assert todo.completed == todo_dict['completed']


def test_todo_normalize():
    todo_normalizer: ToDoNormalizer = ToDoNormalizer()
    todo = ToDo(2, 2, "delectus aut autem", False)
    todo_dict = todo_normalizer.normalize(todo)
    assert isinstance(todo_dict, dict)
    assert todo.userId == todo_dict['userId']
    assert todo.id == todo_dict['id']
    assert todo.title == todo_dict['title']
    assert todo.completed == todo_dict['completed']
