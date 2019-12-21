#!/bin/sh
basedir=$(cd $(dirname $0); pwd)
logdir=$basedir/logs
piddir=$basedir/pid
projectdir=${basedir%script*}
projectname=blog_code
echo $logdir
echo $projectdir
echo $piddir

cd $projectdir
celery multi stop worker1 -A $projectname --logfile=$logdir/work.log --pidfile=$piddir/work.pid
