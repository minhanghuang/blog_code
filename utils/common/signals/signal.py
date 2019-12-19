from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db.backends.signals import connection_created
from django.db.models.signals import pre_migrate, post_migrate
from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception
from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate
from django.test.signals import setting_changed
from django.test.signals import template_rendered
from django.db.backends.signals import connection_created





@receiver(post_migrate)
def callback_post_migrate(sender, **kwargs):
    print("这里是--post_migrate--")
    return None

