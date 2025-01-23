#!/bin/bash

case "$SERVICE" in
   "web")
      python manage.py makemigrations
      python manage.py migrate
      python manage.py collectstatic --no

      gunicorn oms.wsgi:application --bind 0.0.0.0:8000
   ;;
esac
