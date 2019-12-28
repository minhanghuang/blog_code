from app.utils.common.mixins.mixin import MyAPIView
from rest_framework.response import Response
from rest_framework import status
from app.utils.common.cacheredis.cacheredis import my_redis
from blog_code.config import myconfig
from app_article import models
from app_user.models import UserData
import os




class InitApiView(MyAPIView):
    """系统初始化"""

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限
    msg_api = "系统初始化成功"

    def post(self, request):
        """
        该接口只能调用一次, 调用后上锁
        :param request:
        :return:
        """
        if self.get_lock():
            return Response({
                "success": False,
                "msg": "来晚了,兄弟",
                "results": ""
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.my_init() # 1 自定义初始化
        self.init_user(request) # 2 初始化用户
        self.init_data() # 3 初始化个人中心
        self.set_lock() # 99 用完一次后,锁住,禁止使用该接口

        # self.test()

        return Response({
            "success": True,
            "msg": self.msg_api,
            "results": {
                "admin_password":self.admin_password,
                "admin_username":self.admin_username,
            }
        }, status=status.HTTP_200_OK)

    def my_init(self):
        """
        自定义初始化
        :return: None
        """
        self.data_user = myconfig.get_sysinit_data()["user"] # 获取指标文件的数据
        self.data_data = myconfig.get_sysinit_data()["data"] # 获取指标文件的数据
        self.coco_cache_data_field = myconfig.get_sysinit_data()["cache"]["field"]["init"]["coco"] # 获取指标文件cache缓存字段
        self.admin_cache_data_field = myconfig.get_sysinit_data()["cache"]["field"]["init"]["admin"] # 获取指标文件cache缓存字段

        return None

    def get_lock(self):
        """
        获取锁,获取成功,可以使用该接口,否则禁止使用
        :return: bool
        """

        value = my_redis.str_get("init_system")

        return value

    def set_lock(self):
        """
        上锁
        :return: None
        """

        my_redis.str_set("init_system", "1")

        return None


    def set_admin_password(self,request):
        """
        设置管理员密码
        :return: None
        """

        self.admin_password = request.data.get("password","haha123456")

        return None

    def init_user(self, request):
        """
        初始化用户
        新增两个用户, 一个是超级管理员, 一个是游客
        :return: None
        """

        self.set_admin_password(request) # 设置管理员密码
        for foo in self.data_user:
            if foo["username"] == "admin":
                foo["password"] = self.admin_password # 设置密码
                foo["email"] = "job@minhung.me" # 设置邮箱
                foo["is_superuser"] = True # 设置超级管理员
                foo["role"] = 0 # 设置管理员
                self.admin_username = foo["username"]
            models.UserProfile.objects.create_user(**foo)

        return None

    def init_data(self):
        """
        初始化个人中心,必须放在init_user之后
        :return: None
        """

        obj_admin = models.UserProfile.objects.get(username="admin")
        UserData.objects.create(user=obj_admin, **self.data_data)

        obj_coco = models.UserProfile.objects.get(username="coco")
        UserData.objects.create(user=obj_coco, **self.data_data)

        data = {}
        data.update(self.data_data)
        data.update(self.data_user[0])
        self.set_data_cache(self.coco_cache_data_field,str(data)) # 设置coco数据缓存
        self.set_data_cache(self.admin_cache_data_field,str(data)) # 设置admin数据缓存

        return None

    def set_data_cache(self, key="coco", value=""):
        """
        设置coco数据缓存
        :param key: 键名
        :param value: 数据
        :return: None
        """

        my_redis.hash_set("init_data_cache", key, value) # 写入redis

        return None


    def test(self):

        return None

