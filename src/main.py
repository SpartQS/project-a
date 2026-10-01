from flask import Flask

from project_b_utils.date_utils import get_current_date
from project_b_utils.string_utils import reverse_string, capitalize_words, count_words
from project_b_utils.file_utils import read_file, write_file
from project_b_utils.logger_utils import get_logger

app = Flask(__name__)

logger = get_logger("project-a")


@app.route("/")
def home():
    text = "Hello World"

    # Работа со строками
    reversed_text = reverse_string(text)
    capitalized_text = capitalize_words(text)
    words_count = count_words(text)

    # Работа с файлом
    filename = "task.txt"
    write_file(filename, "Файл успешно создан и записан.")
    file_text = read_file(filename)

    # Логирование
    logger.info("Главная страница открыта")

    # Работа с датой
    current_date = get_current_date()

    return f"""
    <h1>Task Manager</h1>

    <p>Сегодня: {current_date}</p>

    <h3>Работа со строками</h3>
    <p>Исходный текст: {text}</p>
    <p>Обратный текст: {reversed_text}</p>
    <p>С заглавной: {capitalized_text}</p>
    <p>Количество слов: {words_count}</p>

    <h3>Работа с файлами</h3>
    <p>{file_text}</p>

    <h3>Логирование</h3>
    <p>Запись в журнал выполнена.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)