from django.db import models
from user_app.models import UserProfile

class Tag(models.Model):
    name = models.CharField(
        verbose_name="标签名",
        max_length=16,
        default=""
    )
    class Meta:
        db_table = 'article_app_Tag' # 数据库名

class Article(models.Model):
    user = models.ForeignKey(
        verbose_name="博主",to=UserProfile,on_delete=models.DO_NOTHING,
    )
    title = models.CharField(
        verbose_name="标题",
        max_length=64,
        default="默认标题",
    )
    content = models.TextField(
        verbose_name="内容",
        default=""
    )
    starttime = models.DateTimeField(
        verbose_name="开始时间",
        auto_now_add=True
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now=True,
    )
    tag = models.ManyToManyField(
        verbose_name="标签",to=Tag,default=""
    )
    titleimage = models.ImageField(
        verbose_name="标题图片",
        default=""
    )
    contentimage = models.ImageField(
        verbose_name="内容图片",
        default=""
    )
    city = models.CharField(
        verbose_name="定位",
        max_length=64,
        default=""
    )
    pageviews = models.IntegerField(
        verbose_name="浏览量",
        default=0
    )

    class Meta:
        db_table = 'article_app_Article' # 数据库名