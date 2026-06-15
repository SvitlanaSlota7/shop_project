Проект написаний на Django 5, використовує PostgreSQL через сучасний драйвер psycopg, налаштований за допомогою django-environ та має інтеграцію з Telegram-API.

Markdown
# Shop Project 🛒

Веб-додаток для інтернет-магазину на базі Django з автоматичним збереженням замовлень у базу даних PostgreSQL та миттєвим сповіщенням у Telegram (через Telegram API).

## 🚀 Функціонал
* **Форма замовлення:** Збір контактних даних користувача на фронтенді (HTML/CSS).
* **База даних:** Надійна архітектура збереження замовлень у PostgreSQL.
* **Telegram нотифікації:** Автоматичне відправлення деталей кожного замовлення власнику магазину або в робочий канал.
* **Безпека:** Усі чутливі дані (паролі, токени, ключі) ізольовані у файлі `.env`.

---

## 🛠️ Технологічний стек
* **Backend:** Python 3.14+ / Django 5.0+
* **Database:** PostgreSQL
* **DB Driver:** Psycopg 3 (Binary)
* **Environment Variables:** Django-environ
* **Frontend:** HTML5, CSS3 

---

## 📋 Інструкція із розгортання та запуску

### 1. Клонування проекту та перехід у директорію
```bash
git clone <посилання_на_мій_репозиторій>
cd shop_project

2. Створення та активація віртуального середовища (venv)

python -m venv venv
# Для Windows (PowerShell):
.\venv\Scripts\Activate.ps1

3. Встановлення залежностей

pip install -r requirements.txt
# Встановлено сучасний драйвер бази даних:
pip install psycopg[binary]

4. Налаштування змінних оточення (.env)
Створюю файл .env у кореневій папці проекту (/shop_project/.env) та заповнюю його за зразком:

DEBUG=True
SECRET_KEY=your_django_secret_key_here

DB_NAME=shop_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather
TELEGRAM_CHANNEL_ID=your_personal_chat_id_or_channel_id

5. Запуск міграцій (Створення таблиць у базі даних)

python manage.py makemigrations
python manage.py migrate

6. Створення адміністратора сайту (Суперкористувача)

python manage.py createsuperuser

7. Запуск локального веб-сервера

python manage.py runserver

Після цього відкриваю браузер та переходжу за адресою: http://127.0.0.1:8000/


📂 Структура проекту

shop_project/
│
├── shop_project/          # Головна папка налаштувань Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Налаштовую базу даних PostgreSQL та .env
│   ├── urls.py            # Головні маршрути
│   └── wsgi.py
│
├── orders/                # Додаток для обробки замовлень 
│   ├── migrations/
│   │            └── 0001_initial.py                   
│   │            └── __init__.py
│   │
│   ├── templates/         # Папка для HTML
│   │           └── index.html     # Форма замовлення
│   ├── __init__.py
│   ├── admin.py           # Реєстрація моделей для адмінки
│   ├── apps.py
│   ├── models.py          # Структура таблиць бази даних (ORM)
│   ├── tests.py
│   └── views.py           # Логіка обробки форми та відправки в Telegram
│
├── static/                # Статичні файли
│        └── css/
│              └── style.css      # Стилі сторінки замовлення
│
├── venv              # Віртуальне середовище 
├── .env              # Секретні токени та паролі до БД
├── .gitignore     # Вказує Git, які файли та папки не потрібно відстежувати та завантажувати на GitHub 
├── manage.py              # Скрипт керування Django
├── README.md           # Опис проекту
└── requirements.txt       # Залежності проекту

