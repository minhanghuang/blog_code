from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from user_app import models
from rest_framework import status
from utils.common.mixins.mixin import MyAPIView
from rest_framework.response import Response
from user_app.api.login.login_serializer import LoginSerializerCls




"""
1. 用户登录接口
"""
class LoginViewSetCls(MyAPIView):
    authentication_classes = () # 验证token, 不需要验证
    permission_classes = () # 权限, 不需要权限
    serializer_class = LoginSerializerCls # 序列化
    jsonschema_dict = {"username": "string", "password": "string"} # 校验传进来的数据
    msg_api = "登录成功"

    def initial(self, request, *args, **kwargs):
        """
        登录初始化
        1. 校验PostData数据
        2. 校验用户名和密码
        """
        super(LoginViewSetCls,self).initial(request, *args, **kwargs) # 基类初始化
        # self.check_json_data(request.data, self.jsonschema_dict)  # 校验postdata的数据
        # self.check_username(**request.data) # 校验用户名和密码是否正确

    def post(self,request):
        playload = request.data
        serializer = self.get_serializer(data=playload)
        self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
        token = self.create_token(self.get_user_obj(username=playload["username"])) # 获取 token
        return Response({
            "success": True,
            "msg": self.msg_api,
            "results": {
                "TOKEN":token,
            }
        }, status=status.HTTP_200_OK)







