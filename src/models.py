class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.title} — {status}"