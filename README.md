# VDNKH-Larsan
Составление маршрутов по ВДНХ, основанные на актуальной афише мероприятий. Интерактивная карта показывает и загруженность ВДНХ.

### Технологический стек:
- Python 3.9+
- Django 4
- PostgreSQL

### Функционал
- Регистрация и авторизация
- Сохранение данных о пользователе для оценки его предпочтений
- Профиль пользователя
- Составление персонализированного маршрута


### Инструкция по настройке проекта
1. Склонировать проект
2. Открыть проект в PyCharm с настройками по умолчанию
3. Создать виртуальное окружение (settings -> project "VDNKH-Larsan" -> project interpreter)
4. Открыть терминал в PyCharm, проверить, что виртуальное окружение активировано
5. Обновить pip:
```commandline
pip install --upgrade pip
```
6. Установить в виртуальное окружение необходимые пакеты:
```
pip install -r requirements_dev.txt
```
7. Скопировать файл `.env.example` в файл `.env` и указать все данные для доступа. Без этого файла проект не запустится.
8. Синхронизировать структуру базы данных с моделями в директории с manage.py:
```
python manage.py migrate
```
9. Создать superuser - пользователя с администраторскими правами, чтобы был доступ к панели администратора django
```
python manage.py createsuperuser
```
10. Создать конфигурацию запуска в PyCharm (файл manage.py, опция runserver)
11. По ссылке http://127.0.0.1:8000/upload/ необходимо загрузить export.json, который был дан вместе с ТЗ. Через него загрузятся популярные маршруты ВДНХ.

### Документация используемых инструментов

- https://docs.djangoproject.com/en/4.1/
- https://postgrespro.ru/docs/postgresql
- https://getbootstrap.com/docs/4.1/getting-started/introduction/
- https://pypi.org/project/psycopg2/
- https://pypi.org/project/python-dotenv/
- https://django-taggit.readthedocs.io/en/latest/