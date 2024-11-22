default:
  just --list

run:
  poetry run python3 madhouse/manage.py runserver

makemigrations:
  poetry run python3 madhouse/manage.py makemigrations

migrate:
  poetry run python3 madhouse/manage.py migrate

admin:
  poetry run python3 madhouse/manage.py createsuperuser
