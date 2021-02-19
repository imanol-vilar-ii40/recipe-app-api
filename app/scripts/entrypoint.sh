# #!/bin/sh

# set -e

# python manage.py migrate --noinput
# python manage.py collectstatic --noinput

# uwsgi --socket :8000 --master --enable-threads --module app.wsgi

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
python manage.py migrate --noinput

exec "$@"