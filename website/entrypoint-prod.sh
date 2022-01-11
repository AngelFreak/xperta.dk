#!/bin/sh
python manage.py collectstatic -v 2 --noinput
gunicorn --bind 0.0.0.0:8000 --workers 3 website.wsgi:application

exec "$@"