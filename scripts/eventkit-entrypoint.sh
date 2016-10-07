#!/bin/bash

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata eventkit/fixtures/admin_user.json
python manage.py runserver 0.0.0.0:8000
