#!/bin/bash
set -e
LOGFILE=/srv/webapps/{{ project_name }}_project/logs/celery_beat.log
LOGDIR=$(dirname $LOGFILE)
# user/group to run as
USER=www-data
GROUP=www-data
cd /srv/webapps/{{ project_name }}_project/{{ project_name }}/
source ./env/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
chown $USER:$GROUP $LOGFILE
export DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
exec ./env/bin/celery beat -A supotsu --uid=$USER --gid=$GROUP -l info --logfile=$LOGFILE 2>>$LOGFILE
