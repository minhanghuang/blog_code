from rest_framework import status
from rest_framework.response import Response
from utils.common.mixins.mixin import APIViewModel
from app_article import models







class GetStateViewSet(APIViewModel):
    """获取文章状态数量"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限

    msg_api = "获取文章状态数量" # 提示信息

    def get(self,request):
        results_dict = {}
        qrticle_list = models.Article.objects.all()
        results_dict["all"] = len(qrticle_list.exclude(state=3))
        results_dict["public"] = len(qrticle_list.filter(state=1))
        results_dict["private"] = len(qrticle_list.filter(state=2))
        results_dict["draft"] = len(qrticle_list.filter(state=0))


        return Response({
            "success": False,
            "msg": "获取文章状态数量",
            "results": results_dict
        }, status=status.HTTP_200_OK)
