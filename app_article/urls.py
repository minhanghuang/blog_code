from django.urls import path
from django.urls import include
from rest_framework import routers

from app_article.views.api.create_article.create_article_viewset import CreateArticleViewSet
from app_article.views.api.list_article.list_article_viewset import ListArticleViewSet
from app_article.views.api.detail_article.detail_article_viewset import DetailArticleViewSet
from app_article.views.api.delete_article.delete_article_viewset import DeleteArticleViewSet
from app_article.views.api.update_article.update_article_viewset import UpdateArticleViewSet
from app_article.views.api.update_image.update_image_viewset import UpdateImageViewSet
from app_article.views.api.update_article_msg.update_article_msg_viewset import UpdateArticleMsgViewSet



CreateArticleViewSetRouter = routers.DefaultRouter()
CreateArticleViewSetRouter.register('', CreateArticleViewSet,base_name="")
ListArticleViewSetRouter = routers.DefaultRouter()
ListArticleViewSetRouter.register('', ListArticleViewSet,base_name="")
DetailArticleViewSetRouter = routers.DefaultRouter()
DetailArticleViewSetRouter.register('', DetailArticleViewSet,base_name="")
DeleteArticleViewSetRouter = routers.DefaultRouter()
DeleteArticleViewSetRouter.register('', DeleteArticleViewSet,base_name="")
UpdateArticleViewSetRouter = routers.DefaultRouter()
UpdateArticleViewSetRouter.register('', UpdateArticleViewSet,base_name="")
UpdateImageViewSetRouter = routers.DefaultRouter()
UpdateImageViewSetRouter.register('', UpdateImageViewSet,base_name="")
UpdateArticleMsgViewSetRouter = routers.DefaultRouter()
UpdateArticleMsgViewSetRouter.register('', UpdateArticleMsgViewSet,base_name="")


urlpatterns = [
    path('create-article/', include(CreateArticleViewSetRouter.urls)), # 发布文章
    path('list-article/', include(ListArticleViewSetRouter.urls)), # 获取文章列表
    path('detail-article/', include(DetailArticleViewSetRouter.urls)), # 获取文章详细信息
    path('delete-article/', include(DeleteArticleViewSetRouter.urls)), # 删除文章
    path('update-article/', include(UpdateArticleViewSetRouter.urls)), # 更新文章
    path('update-image/', include(UpdateImageViewSetRouter.urls)), # 更新图片
    path('update-msg-article/', include(UpdateArticleMsgViewSetRouter.urls)), # 更新文章弹框信息 (注意路由,匹配问题)
]
