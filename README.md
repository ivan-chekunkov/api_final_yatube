# Проект «API для Yatube».

## Описание

Проект реализован на REST API DJANGO. Для аутентификации используйте JWT-токены. 
У неаутентифицированных пользователей доступ к API только на чтение. 
Аутентифицированным пользователям разрешено изменение и удаление своего контента.
Хранение данных в базе SQLite.

## Установка
```bash
# Склонируйте репозиторий
git clone <название репозитория>

# Создайте виртуальное окружение и активируйте его
python -m venv venv
source venv/Scripts/activate

# Установите необходимые пакеты
pip install -r requirements.txt
```
## Локальный запуск
```bash
# Выполнить миграции
python yatube_api/manage.py makemigrations
python yatube_api/manage.py migrate

# Запустить сервер
python yatube_api/manage.py runserver