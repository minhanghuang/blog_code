#!/bin/bash
current_dir=$(cd $(dirname $0); pwd) # 获取当前文件路径
project_dir=${current_dir%script*} # 截取当前文件路径, 只获取项目的根目录

case $1 in
   start) cd $project_dir && celery multi start worker1 -A blog_code && celery -A blog_code beat -l info >  out.file  2>&1  & ;;
   stop) ps -ef |grep celery |grep beat |grep blog_code |awk '{print $2}' | xargs kill -9 && ps -ef |grep celery |grep worker |grep blog_code |awk '{print $2}' | xargs kill -9 ;;
   *) echo "require start|stop" ;;
esac

