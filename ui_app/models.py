from django.db import models

class Ui(models.Model):
    title = models.TextField(
        verbose_name="Ui标题",
        default="起风了"
    )

    class Meta:
        db_table = 'ui_app_Ui' # 数据库名