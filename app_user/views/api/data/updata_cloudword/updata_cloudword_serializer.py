from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase
from utils.common.exceptions import exception
from utils.common.files.file import FileBase




class UpdateCloudWordSerializer(MySerializerBase):
    """更新云词图-序列化"""

    cloudword = serializers.SerializerMethodField(
        label="图片路径",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.UserData
        fields = ["cloudword",]

    def get_avatar(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.cloudword

    def update(self, instance, validated_data):



        return instance







