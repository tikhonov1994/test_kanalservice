# **Тестовое задание в компанию Каналсервис**
Скрипт получает данные из [документа](https://docs.google.com/spreadsheets/d/1jQb-XaDfeQmfB5LazkfXhY6uy3KFt3Ld/edit#gid=1938592304) и сохраняет их в СУБД на основе PostgreSQL.

К данным добавлена колонка «стоимость в руб.», данные по курсу получены от [ЦБ РФ](https://www.cbr.ru/development/SXML/)

В случаях, когда прошел срок поставки, скрипт отправляет уведомление в Telegram.

Для обновления данных и настройки срока отправки уведомлений необходимо настроить периодичность [задач](http://127.0.0.1/admin/django_celery_beat/)

## Инструкция по запуску
* Скачать репозиторий `git clone https://github.com/tikhonov1994/test_kanalservice`
* Перейти в папку test_kanalservice/ `cd test_kanalservice/`
* Создать файл .env и заполнить его (для тестов можно использовать следующие данные):

SQL_ENGINE=django.db.backends.postgresql

SQL_DATABASE=postgres

SQL_USER=postgres

SQL_PASSWORD=postgres

SQL_HOST=db

SQL_PORT=5432

CELERY_BROKER=redis://redis:6379/0

CACHE_LOCATION=redis://redis:6379/0

CHAT_ID=**ID чата в telegram**

TOKEN=**Токе бота в telegram**

* Собрать контейнер и запустить: `docker-compose up --build`
* Провести миграции: `docker-compose exec web python manage.py migrate`
* Создать суперпользователя: `docker-compose exec web python manage.py createsuperuser`
* Собрать статику: `docker-compose exec web python manage.py collectstatic --no-input`