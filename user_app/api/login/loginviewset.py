from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from user_app import models
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from utils.common.mixins.mixin import MyAPIView
from rest_framework.response import Response
from user_app.api.login.loginserializer import LoginSerializerCls

class LoginViewSetCls(MyAPIView):

    serializer_class = LoginSerializerCls
    msg_api = "登录成功"

    def post(self,request):

        serializer = self.get_serializer(data=request.data)
        self.validation_error(serializer=serializer)  # 自定义Serializer异常处理

        return Response({
            "success": True,
            "msg": self.msg_api,
            "results": None
        }, status=status.HTTP_200_OK)







