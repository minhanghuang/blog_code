#!/bin/sh
case $1 in
   start) cd /Users/coxhuang/Documents/django_code/blog_code/ && celery multi start w1 -A  blog_code -l info && celery -A blog_code beat -l info >  out.file  2>&1  & ;;
   stop) sudo ps -ef |grep celery |grep beat |grep blog_code |awk '{print $2}' | xargs kill -9 && sudo ps -ef |grep celery |grep worker |grep blog_code |awk '{print $2}' | xargs kill -9;;
   *) echo "require start|stop" ;;
esac