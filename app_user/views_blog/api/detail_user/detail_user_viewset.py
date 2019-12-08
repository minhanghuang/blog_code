from utils.common.mixins.mixin import MyRetrieveModelMixin
from app_user.views_blog.api.detail_user.detail_user_serializer import DetailUserSerializerBlog
from app_user import models





class DetailUserViewSetBlog(MyRetrieveModelMixin):
    """查看用户详细信息_客户端"""

    authentication_classes = () # 验证
    permission_classes = () # 权限
    msg_detail = "查看用户详细信息_客户端" # 提示信息
    serializer_class = DetailUserSerializerBlog # 序列化类
    queryset = models.UserProfile.objects.all() # models
    lookup_field = "username" # 用户名

