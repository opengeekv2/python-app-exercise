class ToDo:
    def __init__(
        self,
        userId: int,
        id: int,
        title: str,
        completed: bool
    ):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed
