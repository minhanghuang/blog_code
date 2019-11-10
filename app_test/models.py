from django.db import models
import os,time

def user_directory_path(instance, filename):

    return "images/{}.png".format(str(int(time.time()*1000000)))



class TestModel(models.Model):

    dog = models.CharField(
        max_length=64,
        default=""
    )

    image = models.ImageField(upload_to=user_directory_path,default="")



