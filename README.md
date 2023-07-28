## Рассылка (задание)

Написать на Python 2.7 (другие версии или программы не принимаем) небольшой сервис отправки имейл рассылок.

Возможности сервиса:

1. Отправка рассылок с использованием html макета и списка подписчиков.

2. Для создания рассылки использовать ajax запрос. Форма для создания рассылки заполняется в модальном окне. Использовать библиотеки: jquery, bootstrap.

3. Отправка отложенных рассылок.

4. Использование переменных в макете рассылки. (Пример: имя, фамилия, день рождения из списка подписчиков)

5. Отслеживание открытий писем.

Отложенные отправки реализовать при помощи Celery.


## Запуск приложения

- Клонирем 
```bash
git clone https://github.com/yuri-shemetov/mailing_list.git
```
- В папке "MAILING_LIST" устанавливаем виртуальное окружение. Используем Python 2.7. Активируем его:
```bash
source venv/bin/activate
```
- устанавливаем пакеты
```bash
pip install requirements.txt
```
- Запустить Reddis из docker-compose:
```bash
sudo docker compose -f docker-compose.yml up --build
```
- Переходим в папку SRC: `cd src`. Создаем файл .env и копируем в него следующее (не забываем о настройках): 
```bash
SECRET_KEY = luf3x7(j)gfap^gk2$ldyewo-&19lt=v)pl4q-l_!adqa1zb39
DEBUG = True

REDIS_PORT = 16379
REDIS_HOST = localhost

EMAIL_HOST = YOUR SETTINGS
EMAIL_PORT = YOUR SETTINGS
EMAIL_HOST_USER = YOUR SETTINGS
EMAIL_HOST_PASSWORD = YOUR SETTINGS
EMAIL_USE_TLS = YOUR SETTINGS
```
- Запускаем миграции 
```bash
python manage.py makemigrations
python manage.py makemigrate
```
- Создаем суперюзера для админки и возможности ее дальнейшей настройки
```bash
python manage.py createsuperuser
```
- Запускаем локальный сервер 
```bash
python manage.py runserver
```
- Запускаем celery 
```bash
celery -A proj_settings worker -l INFO
```
- Для создание рассылки ```http://localhost:8000/mails/create/```, перед этим не забыть создать в Админке Подписчиков и Шаблоны 
