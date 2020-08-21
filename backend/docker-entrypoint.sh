#!/bin/bash

# Migrate Django_Cron
echo "Apply database migrations"
python manage.py migrate

# Start Cron Job defined in docker file
echo "Starting cron"
echo "* * * * * /code/cronbash.sh >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
nohup cron -f &

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:80
#Needs a blank line