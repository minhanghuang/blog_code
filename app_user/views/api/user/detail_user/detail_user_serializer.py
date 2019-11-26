from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase




class DetailUserSerializer(MySerializerBase):
    """查看用户详细信息-序列化"""

    role = serializers.CharField(source="get_role_display",)
    avatar = serializers.SerializerMethodField(
        label="头像base64",
        required=False,
        allow_null=True,
    )
    class Meta:
        model = models.UserProfile
        fields = ["username","email","role","description","company","department","position","city","tag","avatar",]

    def get_avatar(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.avatar






