#!/bin/sh

basedir=$(cd $(dirname $0); pwd)
echo $basedir

PROCESS=`ps -ef | grep uwsgi | grep -v grep | grep -v PPID | awk '{ print $2}'`

for i in $PROCESS
do
  echo "kill the process [ $i ]"
  kill -9 $i
done