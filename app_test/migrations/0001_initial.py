# Generated by Django 2.0.7 on 2019-11-10 23:41

import app_test.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog', models.CharField(default='', max_length=64)),
                ('image', models.ImageField(default='', upload_to=app_test.models.user_directory_path)),
            ],
        ),
    ]
