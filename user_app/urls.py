from django.urls import path
from django.urls import include
from rest_framework import routers
from user_app.api.login.loginviewset import LoginViewSetCls




# postShoppingCarViewRouter = routers.DefaultRouter()
# postShoppingCarViewRouter.register('', postShoppingCarView)


urlpatterns = [
    path('login/', LoginViewSetCls.as_view()),
]
