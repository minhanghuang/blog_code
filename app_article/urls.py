from django.urls import path
from django.urls import include
from rest_framework import routers

from app_test.views.api.create.create_test_viewset import CreateTestViewSet




CreateTestViewSetRouter = routers.DefaultRouter()
CreateTestViewSetRouter.register('', CreateTestViewSet,base_name="")





urlpatterns = [
    path('create/', include(CreateTestViewSetRouter.urls)),
]
