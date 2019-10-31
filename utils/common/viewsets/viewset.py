from app_user import models
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class MyGenericAPIView(APIView,MyViewBase):

    authentication_classes = ()
    permission_classes = ()
    serializer_class = None
    msg_api = "Ok"

    def get_user_obj(self, username=None):
        """
        获取用户对象,使用前,请先校验用户名密码是否正确
        不在本函数中校验用户名,因为有可能会有多个使用用户名校验,导致重复
        用户名校验,在使用这个接口的时候,在最开头的地方校验
        :param username: 用户名
        :return: 用户对象
        """
        user = models.UserProfile.objects.get(username=username)

        return user

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        return self.serializer_class

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
