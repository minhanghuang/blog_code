from django.urls import path
from django.urls import include
from rest_framework import routers

from app_user.views.api.user.create_user.create_user_viewset import CreateUserViewSet
from app_user.views.api.user.list_user.list_user_viewset import ListUserViewSet
from app_user.views.api.login.login_viewset import LoginUserViewSet
from app_user.views.api.user.detail_user.detail_user_viewset import DetailUserViewSet

LoginUserViewSetRouter = routers.DefaultRouter() # 登录
LoginUserViewSetRouter.register('', LoginUserViewSet,base_name="")
CreateUserViewSetRouter = routers.DefaultRouter() # 新增用户
CreateUserViewSetRouter.register('', CreateUserViewSet,base_name="")
ListUserViewSetRouter = routers.DefaultRouter() # 查看用户列表
ListUserViewSetRouter.register('', ListUserViewSet,base_name="")
DetailUserViewSetRouter = routers.DefaultRouter() # 查看用户详细信息
DetailUserViewSetRouter.register('', DetailUserViewSet,base_name="")



urlpatterns = [
    path('login/', include(LoginUserViewSetRouter.urls)), # 登录
    path('create-user/', include(CreateUserViewSetRouter.urls)), # 新增用户
    path('list-user/', include(ListUserViewSetRouter.urls)), # 查看用户列表
    path('detail-user/', include(DetailUserViewSetRouter.urls)), # 查看用户详细信息
]
