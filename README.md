# RssReader (lab02)
[![Python](https://img.shields.io/badge/python-3.6.5-green.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-2.1.1-orange.svg)](https://www.djangoproject.com/)
[![PythonAnywhere](https://img.shields.io/badge/python-anywhere-blue.svg)]()

Вторая лабораторная работа по учебному курсу "Языки и методы программирования"

Данное приложение представляет собой веб-сервис для чтения rss-лент.
Пользователи имеют возможность добавлять каналы, устанавливать категории и производить поиск по ключевым словам.

## Начало работы

Эта инструкция расскажет о том, как установить проект и начать с ним работу.

### Предварительные настройки

Прежде всего необходимо установить Django

``` 
pip install Django
```

### Установка

Копируем репозиторий

```
git clone https://github.com/Old1906/RssReader-lab02-
```
Переходим в корень

```
cd RssReader-lab01-/RssReader
```

И запускаем сервер

```
python3 manage.py runserver
```

Теперь можно перейти по ссылке и начинать работу

```
http://127.0.0.1:8000/rss
```

## Использовано в работе

* [Django](https://www.djangoproject.com) - Фреймворк для веб-приложений на языке Python.
* [Uikit](https://getuikit.com/) - Интерфейсный фреймворк для разработки веб-интерфейсов.

## Автор

* **Дудник Олег** - ПМ-1701 - [Old1906](https://github.com/Old1906)

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).
