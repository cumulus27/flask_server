#!/bin/sh
#source /home/zte/anaconda3/bin/activate flask_server
source /home/py/local/anaconda3/bin/activate flask

while true; do
    flask deploy
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn -b :5000 --access-logfile - --error-logfile - flask_server:app
