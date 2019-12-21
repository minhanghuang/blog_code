from celery import shared_task
from datetime import datetime
now = datetime.now()
from app.utils.common.cacheredis.cacheredis import my_redis
import time
from app_test.models import TestModel

@shared_task
def text(a,b):

    c = a+b
    my_redis.set("1",c)
    time.sleep(10)
    TestModel.objects.create(dog=now)
    return "1111"

@shared_task
def text2(a,b):

    c = a+b
    my_redis.set("1",c)
    time.sleep(10)
    TestModel.objects.create(dog=now)
    return "22222"
