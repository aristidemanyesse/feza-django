#!/bin/bash
# weed mount -filer="fs-filer-1:8888,fs-filer-2:8888,fs-filer-3:8888" -nonempty -dataCenter="jdc.1" -dir=/vfs -filer.path=/jool/back -allowOthers &
service cron start
yes | python3 manage.py makemigrations
yes | python3 manage.py migrate
#python manage.py patch
python3 manage.py crontab add
python3 manage.py runserver 0.0.0.0:8000

#gunicorn -b 0.0.0.0 --timeout 600 --log-level debug --env DJANGO_SETTINGS_MODULE=jmonitorp.settings jmonitorp.wsgi