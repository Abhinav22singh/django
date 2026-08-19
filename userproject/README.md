# userproject

A basic Django project with a `home` app implementing login/logout-gated access to a home page.

## Requirements

- Python 3.10+
- Django 6.1

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install django
```

## Running

```bash
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin access
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Project structure

```
config/         Project settings, root URLconf, WSGI/ASGI entry points
home/           App with views for index, login, and logout
templets/       HTML templates (index.html, login.html)
static/         Static assets (CSS/JS/images)
db.sqlite3      SQLite database
```

## Routes

| Path      | View                | Description                          |
|-----------|---------------------|---------------------------------------|
| `/`       | `home.views.index`  | Home page; redirects to login if unauthenticated |
| `/login`  | `home.views.login_view` | Login form and authentication |
| `/logout` | `home.views.logout_view` | Logs the user out |
| `/admin/` | Django admin         | Django's built-in admin site |

## Notes

- `DEBUG = True` and the `SECRET_KEY` in `config/settings.py` are development-only defaults — replace both before deploying.
- Database is SQLite (`db.sqlite3`) via Django's default backend.
