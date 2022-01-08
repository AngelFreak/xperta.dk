#!/bin/sh

gunicorn --bind 0.0.0.0:8000 --workers 3 website.wsgi:application

exec "$@"