#!/bin/bash


# don't forget to add this script to the /etc/crontab:
#
# */1 * * * * username /home/django/tola-help/scripts/get_email.sh >> /tmp/foo.log 2>&1

# set your django and project paths here
PATHTODJANGO="/usr/lib/python2.7/dist-packages/django/"
PATHTOPROJECT="/home/django/tola-help/"


export PYTHONPATH=$PYTHONPATH:$PATHTODJANGO:$PATHTOPROJECT:

cd $PATHTOPROJECT
/usr/bin/python manage.py get_email