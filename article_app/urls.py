from django.urls import path
from django.urls import include
from rest_framework import routers
from article_app.api.CDUL.createarticle.create_article_viewset import CreateArticleViewSetCls
from article_app.api.CDUL.listarticle.get_article_list_viewset import GetArticleListViewSetCls
from article_app.api.CDUL.detailarticle.get_article_detail_viewset import GetArticleDetailViewSetCls
from article_app.api.CDUL.deletearticle.del_article_viewset import DelArticleViewSetCls
from article_app.api.CDUL.updatearticle.update_article_viewset import UpdateArticleViewSetCls



CreateArticleViewSetClsRouter = routers.DefaultRouter() # 新建博文
CreateArticleViewSetClsRouter.register('', CreateArticleViewSetCls,base_name="")
GetArticleListViewSetClsRouter = routers.DefaultRouter() # 货物博文列表
GetArticleListViewSetClsRouter.register('', GetArticleListViewSetCls,base_name="")
GetArticleDetailViewSetClsRouter = routers.DefaultRouter() # 获取博文详细信息
GetArticleDetailViewSetClsRouter.register('', GetArticleDetailViewSetCls,base_name="")
DelArticleViewSetClsRouter = routers.DefaultRouter() # 删除博文
DelArticleViewSetClsRouter.register('', DelArticleViewSetCls,base_name="")
UpdateArticleViewSetClsRouter = routers.DefaultRouter() # 修改博文
UpdateArticleViewSetClsRouter.register('', UpdateArticleViewSetCls,base_name="")


urlpatterns = [
    path('createarticle/',include(CreateArticleViewSetClsRouter.urls)), # 新建博文
    path('getarticlelist/',include(GetArticleListViewSetClsRouter.urls)), # 货物博文列表
    path('getarticledetail/',include(GetArticleDetailViewSetClsRouter.urls)), # 获取博文详细信息
    path('delarticle/',include(DelArticleViewSetClsRouter.urls)), # 删除博文
    path('updatearticle/',include(UpdateArticleViewSetClsRouter.urls)), # 修改博文
]
