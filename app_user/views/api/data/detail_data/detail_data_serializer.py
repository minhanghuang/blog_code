from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase
from utils.common.exceptions import exception
from utils.common.files.file import FileBase




class DetailDataSerializer(MySerializerBase):
    """查看data详细信息-序列化"""

    cloudword = serializers.SerializerMethodField(
        label="图片base64",
        required=False,
        allow_null=True,
    )


    class Meta:
        model = models.UserData
        fields = ["cloudword","tag",]

    def get_cloudword(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.cloudword








