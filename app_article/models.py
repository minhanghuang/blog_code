from django.db import models
from app_user.models import UserProfile
import time,random

def upload_images_path(instance, filename):
    """
    生成图片文件名
    :param instance: None
    :param filename: 前端传来的文件的原始文件名
    :return: 拼接后生成的文件名和存储路径
    """
    if not filename: # 如果图片为空 -> 给随机默认图片
        print("没有上传图片")
        return "images/blog/default/{}.png".format(random.randint(1, 7))

    print("上传图片成功")
    last = filename.split(".")[1]
    return "images/blog/{}.{}".format(str(int(time.time() * 1000000)), last)


def default_images_path():
    print("ppppp")
    return "images/blog/default/{}.png".format(random.randint(1, 7))





class Article(models.Model):
    """博文"""
    state_choices = (
        (0, "草稿箱"),
        (1, "公开"),
        (2, "秘密"),
    )

    author = models.ForeignKey(
        to=UserProfile,
        on_delete=models.DO_NOTHING,
        related_name="article_author",
        verbose_name="作者",
    ) # 博文1 -> 作者1; 作者1 -> 博文n; (Fk : 博文)
    title = models.CharField(
        max_length=64,
        default="",
        verbose_name="标题",
    )
    subtitle = models.CharField(
        max_length=64,
        default="",
        verbose_name="副标题",
    )
    content = models.TextField(
        default="",
        verbose_name="内容",
    )
    readcount = models.IntegerField(
        default=0,
        verbose_name="阅读量",
    )
    createdate = models.DateTimeField(
        auto_now_add=True, # 更新对象时不会改变
        verbose_name="创建时间",
    )
    updatedate = models.DateTimeField(
        auto_now=True, # 更新对象时会改变
        verbose_name="修改时间",
    )
    state = models.IntegerField(
        default=0,
        choices=state_choices,
        verbose_name="文章状态"
    )
    image = models.ImageField(
        upload_to=upload_images_path,
        default="",
        verbose_name="博文列表展示的图片",
    )

