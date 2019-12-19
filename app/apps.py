from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import utils.common.signals.signal  # signal.py路径
