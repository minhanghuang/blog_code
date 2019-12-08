from django.urls import path
from django.urls import include
from rest_framework import routers

from app_user.views.api.user.create_user.create_user_viewset import CreateUserViewSet
from app_user.views.api.user.list_user.list_user_viewset import ListUserViewSet
from app_user.views.api.login.login_viewset import LoginUserViewSet
from app_user.views.api.user.detail_user.detail_user_viewset import DetailUserViewSet
from app_user.views_blog.api.detail_user.detail_user_viewset import DetailUserViewSetBlog
from app_user.views.api.user.update_user.update_user_viewset import UpdateUserViewSet
from app_user.views.api.user.update_avatar.update_avatar_viewset import UpdateAvatarViewSet

LoginUserViewSetRouter = routers.DefaultRouter() # 登录
LoginUserViewSetRouter.register('', LoginUserViewSet,base_name="")
CreateUserViewSetRouter = routers.DefaultRouter() # 新增用户
CreateUserViewSetRouter.register('', CreateUserViewSet,base_name="")
ListUserViewSetRouter = routers.DefaultRouter() # 查看用户列表
ListUserViewSetRouter.register('', ListUserViewSet,base_name="")
DetailUserViewSetRouter = routers.DefaultRouter() # 查看用户详细信息
DetailUserViewSetRouter.register('', DetailUserViewSet,base_name="")
DetailUserViewSetBlogSetRouter = routers.DefaultRouter() # 查看用户详细信息_客户端
DetailUserViewSetBlogSetRouter.register('', DetailUserViewSetBlog,base_name="")
UpdateUserViewSetRouter = routers.DefaultRouter() # 更新用户详细信息
UpdateUserViewSetRouter.register('', UpdateUserViewSet,base_name="")
UpdateAvatarViewSetRouter = routers.DefaultRouter() # 更新用户头像
UpdateAvatarViewSetRouter.register('', UpdateAvatarViewSet,base_name="")



urlpatterns = [
    path('login/', include(LoginUserViewSetRouter.urls)), # 登录
    path('create-user/', include(CreateUserViewSetRouter.urls)), # 新增用户
    path('list-user/', include(ListUserViewSetRouter.urls)), # 查看用户列表
    path('detail-user/', include(DetailUserViewSetRouter.urls)), # 查看用户详细信息
    path('blog/detail-user/', include(DetailUserViewSetBlogSetRouter.urls)), # 查看用户详细信息_客户端
    path('update-user/', include(UpdateUserViewSetRouter.urls)), # 更新用户详细信息
    path('update-avataruser/', include(UpdateAvatarViewSetRouter.urls)), # 更新用户头像
]
