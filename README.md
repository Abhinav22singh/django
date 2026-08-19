# Django Learning Project

A hands-on Django project built step by step to learn the framework's core
pieces: URL routing, templates, static files, forms, models/ORM, messages
framework, and authentication. The commit history below doubles as a
learning log.

## Stack

| Tool     | Version |
|----------|---------|
| Python   | 3.14    |
| Django   | 6.1     |
| Database | SQLite  |
| Frontend | Bootstrap 5 (CDN) |

## Getting started

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # optional, for /admin
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Project structure

```
config/                 Project-level package: settings, root URLconf, WSGI/ASGI
  settings.py            Django settings (apps, middleware, templates, DB, static)
  urls.py                 Root URL routing -> Home app views
  templets/               Shared HTML templates (base, index, about, contact)
  static/                 Static assets

Home/                    App: home page, about, services, contact
  views.py                View functions
  models.py               Contact model (stores contact-form submissions)
  urls.py                 App-level URLconf (not currently wired into config/urls.py)
  migrations/              DB schema history

userproject/             Earlier/parallel practice project (login + logout flow)
  home/                    App with index / login / logout views
  templets/                index.html, login.html

manage.py                Django's command-line entry point
requirements.txt         Pinned dependencies
db.sqlite3               SQLite database file
```

## Routes (`config/urls.py`)

| Path       | View               | Description                          |
|------------|--------------------|---------------------------------------|
| `/`        | `Home.views.index`    | Home page, shows a flash message via the messages framework |
| `/about`   | `Home.views.about`    | Static about page |
| `/services`| `Home.views.services` | Plain-text services page |
| `/contact` | `Home.views.contact`  | Contact form; `POST` saves a `Contact` row to the DB |
| `/admin/`  | Django admin        | Built-in admin site (branded as "UMSRA Admin") |

## What this project covers so far

Each commit corresponds to a concept that was learned and applied:

1. **`a45f3ce` — URL dispatching**
   Wiring `path()` entries in `urls.py` to view functions; the
   request → URLconf → view → response cycle.

2. **`11f3f2a` — Static files & templates**
   `STATIC_URL` / `STATICFILES_DIRS`, `TEMPLATES['DIRS']`, and rendering
   an HTML template from a view with `render()`.

3. **`df1ac32` — Frontend integration**
   Template inheritance with `{% extends %}` / `{% block %}`, a shared
   `base.html` with a Bootstrap navbar/footer, and multiple pages
   (`index`, `about`, `contact`) built on top of it.

4. **`13081ad` — Contact form working end-to-end**
   A Django **model** (`Contact`) mapped to the DB via **migrations**,
   reading `POST` data with `request.POST.get(...)`, saving a model
   instance, and giving user feedback with the **messages framework**
   (`django.contrib.messages`) rendered as dismissible Bootstrap alerts
   in `base.html`.

5. **`f694e70` — Authentication**
   A second practice app (`userproject`) adding login/logout views
   gated by Django's built-in `django.contrib.auth`.

### Key Django concepts practiced

- **MVT pattern**: models (`Home/models.py`) → views (`Home/views.py`) →
  templates (`config/templets/*.html`).
- **URLconf & routing**: `path()`, named URLs (`name='home'`), and the
  `{% url %}` template tag to avoid hardcoding links.
- **Template inheritance**: one `base.html` shared across pages via
  `{% extends %}` + `{% block body %}`.
- **Forms & CSRF**: `{% csrf_token %}` in every POST form, reading
  submitted fields with `request.POST.get(...)`.
- **ORM basics**: defining a `models.Model` subclass, running
  `makemigrations` / `migrate`, and `.save()`-ing an instance.
- **Messages framework**: `messages.success(request, ...)` + rendering
  `{% if messages %}` in the base template for flash notifications.
- **Django admin**: customizing `admin.site.site_header` /
  `site_title` / `index_title` for a branded admin portal.
- **Static vs. template dirs**: keeping `static/` (CSS/JS/images)
  separate from `templets/` (HTML), each declared explicitly in
  `settings.py`.

## Notes / things to clean up later

- `Home/urls.py` exists but `config/urls.py` currently wires routes to
  `Home.views` directly instead of `include('Home.urls')` — worth
  unifying so all routing goes through the app's own URLconf (see how
  `userproject/config/urls.py` already does this with `include()`).
- `DEBUG = True` and the `SECRET_KEY` in `config/settings.py` are
  development-only defaults — replace both before any real deployment.
- `db.sqlite3` and `__pycache__/` are currently committed; consider
  adding a `.gitignore` for `venv/`, `__pycache__/`, `*.pyc`, and the
  SQLite file going forward.
- `userproject/` is a separate, self-contained Django project (its own
  `manage.py`, `venv/`, `db.sqlite3`) used to practice authentication
  in isolation from the main app.

## Useful commands

```bash
python manage.py runserver          # dev server
python manage.py makemigrations     # generate migration files after model changes
python manage.py migrate            # apply migrations
python manage.py createsuperuser    # create an admin login
python manage.py shell              # interactive shell with app context loaded
```
