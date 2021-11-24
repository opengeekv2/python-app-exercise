from src.model.todo import ToDo
from src.infrastructure.Normalizer import Normalizer


class ToDoNormalizer(Normalizer):
    def denormalize(self, todo_dict: dict) -> ToDo:
        return ToDo(
            todo_dict['userId'],
            todo_dict['id'],
            todo_dict['title'],
            todo_dict['completed']
        )

    def normalize(self, todo: ToDo) -> dict:
        return {
            'userId': todo.userId,
            'id': todo.id,
            'title': todo.title,
            'completed': todo.completed
        }
