#!/bin/bash
# Make sure *.sh scripts have +x set
set -e
LOGFILE=/srv/webapps/{{ project_name }}_project/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=5
# user/group to run as
USER=www-data
GROUP=www-data
cd /srv/webapps/{{ project_name }}_project/{{ project_name }}/
source ./env/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
chown $USER:$GROUP $LOGFILE
export DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
exec ./env/bin/gunicorn {{ project_name }}.wsgi:application -b 127.0.0.1:8787 -w $NUM_WORKERS \
--user=$USER --group=$GROUP --log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE
