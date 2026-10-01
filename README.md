# Project A — Task Manager

Веб-приложение для управления задачами на Python и Flask.

Проект A использует библиотеку Project B для работы с датами, строками, файлами и логированием.

## Технологии

* Python
* Flask
* pytest
* Project B

## Структура проекта

```text
project-a/
├── src/
│   ├── main.py
│   ├── models.py
│   ├── module_loader.py
│   ├── utils.py
│   └── __init__.py
├── tests/
│   └── test_main.py
├── libs/
│   └── project-b/
├── requirements.txt
└── README.md
```

## Установка

Создать виртуальное окружение:

```powershell
python -m venv .venv
```

Активировать виртуальное окружение:

```powershell
.\.venv\bin\Activate.ps1
```

Установить зависимости:

```powershell
pip install -r requirements.txt
```

## Подключение Project B

Project B используется как Python-пакет.

Установка локального пакета:

```powershell
pip install -e ../project-b
```

Также зависимость указана в `requirements.txt`:

```text
-e ../project-b
flask
```

## Запуск

Запустить веб-приложение:

```powershell
python src/main.py
```

После запуска открыть в браузере:

```text
http://127.0.0.1:5000
```

## Функциональность

Веб-приложение демонстрирует использование функций Project B:

* получение текущей даты;
* обработка строк;
* подсчёт слов;
* запись и чтение файлов;
* логирование.

## Тестирование

Запустить тесты:

```powershell
pytest
```

В ходе разработки все тесты были успешно пройдены:

```text
4 passed
```
