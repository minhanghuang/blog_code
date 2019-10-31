from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """用户表"""

    role_choices = (
        (0,"管理员"),
        (1,"游客"),
    )
    role = models.PositiveIntegerField(
        verbose_name="用户角色",
        choices=role_choices,
        default=1,
    )

    class Meta:
        db_table = 'app_user_UserProfile' # 数据库名