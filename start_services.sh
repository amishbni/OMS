#!/bin/bash

case "$SERVICE" in
   "web")
      gunicorn oms.wsgi:application --bind 0.0.0.0:8000
   ;;
esac
