from models import Task
from utils import print_tasks


def main():
    tasks = [
        Task("Изучить Git"),
        Task("Выполнить лабораторную работу"),
        Task("Создать отчёт")
    ]

    print("Список задач:")
    print_tasks(tasks)


if __name__ == "__main__":
    main()