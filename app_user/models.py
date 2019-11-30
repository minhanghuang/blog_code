from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """用户表"""

    role_choices = (
        (0,"管理员"),
        (1,"游客"),
    )
    name = models.CharField(
        default="",
        max_length=64,
        verbose_name="姓名,并非用户名",
    )
    wechat = models.CharField(
        default="",
        max_length=64,
        verbose_name="微信",
    )
    telegram = models.CharField(
        default="",
        max_length=64,
        verbose_name="Tg",
    )
    phone = models.CharField(
        default="",
        max_length=64,
        verbose_name="手机号码",
    )
    role = models.PositiveIntegerField(
        verbose_name="用户角色",
        choices=role_choices,
        default=1,
    )
    description = models.CharField(
        default="",
        max_length=128,
        verbose_name="签名描述",
    )
    company = models.CharField(
        default="",
        max_length=128,
        verbose_name="公司",
    )
    department= models.CharField(
        default="",
        max_length=128,
        verbose_name="部门",
    )
    position = models.CharField(
        default="",
        max_length=128,
        verbose_name="职位",
    )
    city = models.CharField(
        default="",
        max_length=128,
        verbose_name="城市",
    )
    tag = models.TextField(
        default="[]",
        verbose_name="标签",
    )
    avatar = models.TextField(
        default="",
        verbose_name="用户头像",
    )

    class Meta:
        db_table = 'app_user_UserProfile' # 数据库名