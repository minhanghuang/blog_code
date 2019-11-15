from django.db import models
from app_user.models import UserProfile
import time,random,os
from django.conf import settings

# def upload_images_path(instance, filename):
#     """
#     生成图片文件名
#     :param instance: None
#     :param filename: 前端传来的文件的原始文件名
#     :return: 拼接后生成的文件名和存储路径
#     """
#
#     article_id = instance.id # 文章id
#     last = filename.split(".")[1]
#     old_image_path = "".join((settings.MEDIA_ROOT,"/images/blog/{}.{}".format(article_id, last))) # 拼接
#
#     if os.path.exists(old_image_path):
#         os.remove(old_image_path)
#
#     return old_image_path





class Article(models.Model):
    """博文"""
    state_choices = (
        (0, "草稿箱"),
        (1, "公开"),
        (2, "秘密"),
        (3, "已删除"),
    )
    istop_choices = (
        (0, "正常"),
        (1, "置顶"),
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
    image = models.TextField(
        default="",
        verbose_name="文章图片base64二进制流",
    )
    istop = models.IntegerField(
        choices=istop_choices,
        default=0,
        verbose_name="置顶",
    )
    tag = models.CharField(
        default="{}",
        max_length=127,
        verbose_name="标签",
    )
    category = models.CharField(
        default="{}",
        max_length=127,
        verbose_name="文章类别",
    )

