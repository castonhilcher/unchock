#!/bin/bash

while ! nc -z db 5432; do sleep 1; done;

echo "Apply database migrations"
python manage.py migrate

# Start tasks
echo "Starting process_tasks"
nohup python manage.py process_tasks &

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:80
#Needs a blank line