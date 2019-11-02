from utils.common.mixins.mixin import MyCreateModeMixin
from app_test.views.api.create.create_test_serializer import CreateTestSerializer
from rest_framework import status
from rest_framework.response import Response


class CreateTestViewSet(MyCreateModeMixin):
    """新增测试"""
    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_create = "成功新增Test" # 提示信息
    results_display = False  # 是否显示序列化信息, 默认显示
    serializer_class = CreateTestSerializer # 序列化类
