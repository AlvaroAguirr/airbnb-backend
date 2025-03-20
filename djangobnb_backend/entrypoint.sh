#!/bin/sh

if [ "$DATABASE" = "postgres" ] 
then
    echo "check if database is runnning..."

    while ! nc -z $SQL_HOST  $SQL_PORT ; do
        sleep 0.1
    done 

    echo "the database is up and runnint :D"
fi

python manage.py makemigrations
python manage.py migrate


exec "$@"