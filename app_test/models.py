from django.db import models

class TestModel(models.Model):

    dog = models.CharField(
        max_length=64,
        default=""
    )
