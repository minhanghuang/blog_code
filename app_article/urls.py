from django.urls import path
from django.urls import include
from rest_framework import routers

from app_article.views.api.create_article.create_article_viewset import CreateArticleViewSet



CreateArticleViewSetRouter = routers.DefaultRouter()
CreateArticleViewSetRouter.register('', CreateArticleViewSet,base_name="")





urlpatterns = [
    path('create-article/', include(CreateArticleViewSetRouter.urls)),
]
