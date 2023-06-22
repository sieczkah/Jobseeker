#!/bin/sh

set -e

whoami

python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module jobseeker.wsgi
