from django.urls import path
from django.urls import include
from rest_framework import routers

from app_article.views.api.create_article.create_article_viewset import CreateArticleViewSet
from app_article.views.api.list_article.list_article_viewset import ListArticleViewSet
from app_article.views.api.detail_article.detail_article_viewset import DetailArticleViewSet



CreateArticleViewSetRouter = routers.DefaultRouter()
CreateArticleViewSetRouter.register('', CreateArticleViewSet,base_name="")
ListArticleViewSetRouter = routers.DefaultRouter()
ListArticleViewSetRouter.register('', ListArticleViewSet,base_name="")
DetailArticleViewSetRouter = routers.DefaultRouter()
DetailArticleViewSetRouter.register('', DetailArticleViewSet,base_name="")





urlpatterns = [
    path('create-article/', include(CreateArticleViewSetRouter.urls)),
    path('list-article/', include(ListArticleViewSetRouter.urls)),
    path('detail-article/', include(DetailArticleViewSetRouter.urls)),
]
