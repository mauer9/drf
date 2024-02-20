# DRF Snippets API

Dependencies:

- Python v3.11
- DRF v3.14
- PostgreSQL 16

## Project Setup

### Docker

Make sure you've installed Docker v24 or up, Docker Compos v2 or up.

build and run the docker image

```bash
docker compose up
```

### Manual

download the code and install poetry dependencies

```bash
git clone https://github.com/mauer9/drf.git
cd pollster
poetry install
```

migrate database

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

create admin user using this command

```bash
poetry run python manage.py createsuperuser
```

run the app locally

```bash
poetry run python manage.py runserver
```
