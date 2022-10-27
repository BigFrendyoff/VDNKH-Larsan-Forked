# VDNKH-Larsan
Составление маршрутов по ВДНХ, основанный на актуальной афише мероприятий

### Технологический стек:
- Python 3.9+
- Django 4
- PostgreSQL

###Функционал
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
7. Скопировать файл `.env.sample` в файл `.env` и указать все данные для доступа. Без этого файла проект не запустится.
8. Синхронизировать структуру базы данных с моделями:
```
python manage.py migrate
```
9. Создать конфигурацию запуска в PyCharm (файл manage.py, опция runserver)

### Документация используемых инструментов

- https://docs.djangoproject.com/en/4.1/
- https://postgrespro.ru/docs/postgresql
- https://getbootstrap.com/docs/4.1/getting-started/introduction/
- https://pypi.org/project/psycopg2/