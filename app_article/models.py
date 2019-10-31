from django.db import models
from app_user.models import UserProfile

class Article(models.Model):
    """博文"""

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
    content = models.TextField(
        default="",
        verbose_name="内容",
    )
    create_date = models.DateTimeField(
        auto_now_add=True, # 更新对象时不会改变
        verbose_name="创建时间",
    )
    update_date = models.DateTimeField(
        auto_now=True, # 更新对象时会改变
        verbose_name="修改时间",
    )
    is_enable = models.BooleanField(
        default=True,
        verbose_name="是否可见",
    )
