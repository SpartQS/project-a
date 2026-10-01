from flask import Flask, render_template_string

from project_b_utils import (
    get_current_date,
    reverse_string,
    capitalize_words
)

app = Flask(__name__)


HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Task Manager</title>
</head>
<body>
    <h1>Task Manager</h1>

    <p>Сегодня: {{ date }}</p>

    <p>Обратный текст: {{ reversed_text }}</p>

    <p>С заглавной: {{ capitalized }}</p>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(
        HTML,
        date=get_current_date(),
        reversed_text=reverse_string("Hello World"),
        capitalized=capitalize_words("hello world")
    )


if __name__ == "__main__":
    app.run(debug=True)