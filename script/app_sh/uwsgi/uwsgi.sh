#!/bin/sh

basedir=$(cd $(dirname $0); pwd)
stopdir=$basedir/sh

case $1 in
   start) cd $basedir && uwsgi --ini uwsgi.ini ;;
   stop) cd $stopdir && sh stop_uwsgi.sh  ;;
   *) echo "require start|stop" ;;
esac