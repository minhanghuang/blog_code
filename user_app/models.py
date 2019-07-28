from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    """用户表"""
    role_choices = (
        (0,"超管"),
        (1,"博主"),
    )
    role = models.IntegerField(
        verbose_name="用户角色",choices=role_choices,default=1
    )
    image = models.ImageField(
        verbose_name="头像",default=""
    )

    class Meta:
        db_table = 'user_app_UserProfile' # 数据库名



