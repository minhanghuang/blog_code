from rest_framework.mixins import (
    CreateModelMixin,DestroyModelMixin,
    UpdateModelMixin,ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from utils.common.serializers.serializer import SerializerPlug
from utils.common.paginations.pagination import MyPagination
from rest_framework.views import APIView

"""
1. post create data
"""
class MyCreateModeMixin(CreateModelMixin,GenericViewSet,SerializerPlug):
    authentication_classes = ()
    permission_classes = ()
    msg_create = "创建成功"
    results_display = True # 是否显示序列化信息, 默认显示

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True) # Serializer自带的异常处理(不符合我们的需求,需要自定义)
        self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        data = serializer.data if self.results_display else None

        return Response({
            "success": True,
            "msg": self.msg_create,
            "results":data
        }, status=status.HTTP_200_OK)

"""
2. delete destroy data
"""
class MyDeleteModelMixin(DestroyModelMixin, GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    msg_delete = "成功删除"
    lookup_field = "pk" # 主键

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({
            "success": True,
            "msg": self.msg_delete,
            "results": None
        }, status=status.HTTP_200_OK)

"""
3. put update data
"""
class MyUpdateModelMixin(UpdateModelMixin, GenericViewSet,SerializerPlug):
    authentication_classes = ()
    permission_classes = ()
    msg_update = "修改成功"
    lookup_field = "pk" # 主键
    results_display = True

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        # serializer.is_valid(raise_exception=True)
        self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        data = serializer.data if self.results_display else None


        return Response({
            "success": True,
            "msg": self.msg_update,
            "results": data
        }, status=status.HTTP_200_OK)

"""
4. get list data
"""
class MyListModeMixin(ListModelMixin,GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    pagination_class = MyPagination # 分页
    msg_list = "成功获取列表数据"

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "success": True,
            "msg": self.msg_list,
            "results":serializer.data
        }, status=status.HTTP_200_OK)

"""
5. get retrieve data
"""
class MyRetrieveModelMixin(RetrieveModelMixin,GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    msg_detail = "成功获取详细数据"
    lookup_field = "pk" # 主键

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response({
            "success": True,
            "msg": self.msg_detail,
            "results":serializer.data
        }, status=status.HTTP_200_OK)

"""
5. APIView
"""
class MyAPIView(APIView,SerializerPlug):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = None
    msg_api = "Ok"

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

    def post(self,request):
        # serializer = self.get_serializer(data=request.data)
        # self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
        return Response({
            "success": False,
            "msg": "基类POST,请重新封装",
            "results": ""
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        # serializer = self.get_serializer(data=request.data)
        # self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
        return Response({
            "success": False,
            "msg": "基类PUT,请重新封装",
            "results": ""
        }, status=status.HTTP_400_BAD_REQUEST)

