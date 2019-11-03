"""blog_code URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.urls import path
# from rest_framework.schemas import get_schema_view # 导入辅助函数get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer # swagger
# schema_view = get_schema_view(title='API',renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', schema_view, name='docs'),  # 配置swagger的url路径
    path('', include_docs_urls(title='接口文档')),  # coreapi接口路径
    path('api/article/', include('app_article.urls')),
    path('api/user/', include('app_user.urls')),
    path('api/test/', include('app_test.urls')),
]
