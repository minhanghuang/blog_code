from django.urls import path
from django.urls import include
from rest_framework import routers

from app.api.init.init_apiview import InitApiView



urlpatterns = [
    path('init/', InitApiView.as_view()), # 系统初始化
]
