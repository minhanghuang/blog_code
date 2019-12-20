from app.utils.common.mixins.mixin import MyCreateModeMixin
from app_test.views.api.create_imag.create_test_serializer import CreateImagSerializer


class CreateImagViewSet(MyCreateModeMixin):
    """新增图片"""
    authentication_classes = () # 验证
    permission_classes = () # 权限
    msg_create = "新增图片" # 提示信息
    results_display = False  # 是否显示序列化信息, 默认显示
    serializer_class = CreateImagSerializer # 序列化类

    # def post(self,request):
    #
    #     models.TestModel.objects.create(
    #         image = request.data["file"]
    #     )
    #
    #     return Response({
    #         "success": False,
    #         "msg": "新增图片",
    #         "results": ""
    #     }, status=status.HTTP_200_OK)