"""
子类
"""
from utils.common.mixins.mixinbase import (
    CreateModel, DestroyModel,UpdateModel,
    ListModel,RetrieveModel,APIViewModel,
)
from rest_framework.response import Response
from rest_framework import status
from utils.common.paginations.pagination import MyPagination
from app_user import models


class MyCreateModeMixin(CreateModel):
    '''
        retrieve:
            Return a user instance.

        list:
            Return all users,ordered by most recent joined.

        create:
            Create a new user.

        delete:
            Remove a existing user.

        partial_update:
            Update one or more fields on a existing user.

        update:
            Update a user.
    '''
    authentication_classes = ()
    permission_classes = ()
    msg_create = "创建成功"
    results_display = True # 是否显示序列化信息, 默认显示

class MyDeleteModelMixin(DestroyModel):
    authentication_classes = ()
    permission_classes = ()
    msg_delete = "成功删除"
    lookup_field = "pk" # 主键

class MyUpdateModelMixin(UpdateModel):
    authentication_classes = ()
    permission_classes = ()
    msg_update = "修改成功"
    lookup_field = "pk" # 主键
    results_display = True # 是否显示序列化信息, 默认显示

class MyListModeMixin(ListModel):
    authentication_classes = ()
    permission_classes = ()
    pagination_class = MyPagination # 分页
    queryset = models.UserProfile.objects.all() # models
    msg_list = "成功获取列表数据"

class MyRetrieveModelMixin(RetrieveModel):
    authentication_classes = ()
    permission_classes = ()
    msg_detail = "成功获取详细数据"
    lookup_field = "pk" # 主键

class MyAPIView(APIViewModel):

    authentication_classes = ()
    permission_classes = ()
    msg_api = "Ok"




