#!/bin/sh

until nc -z $SQL_HOST $SQL_PORT
do
  echo "Waiting for Postgres..."
  sleep 1
done

echo "Postgres is ready, setting up database..."

python manage.py flush --no-input &&
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py collectstatic --no-input &&

exec "$@"