# Generated by Django 2.0.7 on 2019-11-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_article', '0002_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(default='{}', max_length=127, verbose_name='文章类别'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(default='{}', max_length=127, verbose_name='标签'),
        ),
    ]
