from django.urls import path
from django.urls import include
from rest_framework import routers

from app_test.views.api.create.create_test_viewset import CreateTestViewSet
from app_test.views.api.list.list_test_viewset import ListTestViewSet




CreateTestViewSetRouter = routers.DefaultRouter() # 新增Test
CreateTestViewSetRouter.register('', CreateTestViewSet,base_name="")
ListTestViewSetRouter = routers.DefaultRouter() # 查看Test列表
ListTestViewSetRouter.register('', ListTestViewSet,base_name="")




urlpatterns = [
    path('create/', include(CreateTestViewSetRouter.urls)), # 新增测试
    path('list/', include(ListTestViewSetRouter.urls)), # 查看测试列表
]
