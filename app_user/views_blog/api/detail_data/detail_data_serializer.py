from rest_framework import serializers
from app.utils.common.serializers.serializer import MySerializerBase

from app_user import models


class DetailDataSerializerBlog(MySerializerBase):
    """查看data详细信息-序列化"""

    cloudword = serializers.SerializerMethodField(
        label="图片base64",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.UserData
        fields = ["cloudword","tag","cloudword_width","timeline",]

    def get_cloudword(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.cloudword








