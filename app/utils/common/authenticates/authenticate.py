from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from app_user import models


class CustomBackend(ModelBackend):
    """
    自定义用户验证规则
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = models.UserProfile.objects.get(
                Q(username=username) |
                Q(email=username)
            )
            if user.check_password(password):
                return user
        except Exception as e:
            print("自定义用户验证规则-用户登录验证异常except:", e)
            return None