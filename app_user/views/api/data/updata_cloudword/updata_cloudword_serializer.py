from rest_framework import serializers
from app.utils.common.serializers.serializer import MySerializerBase

from app_user import models


class UpdateCloudWordSerializer(MySerializerBase):
    """更新云词图-序列化"""

    cloudword = serializers.SerializerMethodField(
        label="图片",
        required=False,
        allow_null=True,
    )
    cloudword_width = serializers.SerializerMethodField(
        label="返回图片大小",
        required=False,
        allow_null=True,
    )
    circle = serializers.BooleanField(
        label="图片形状(True:圆形,False:正方形)",
        required=False,
        default=True,
    )
    tag = serializers.CharField(
        label="标签",
        required=False,
        allow_null=True,
    )
    width = serializers.IntegerField(
        label="图片大小",
        required=False,
        allow_null=True,
    )
    color = serializers.CharField(
        label="背景颜色",
        required=False,
        allow_null=True,
    )
    full = serializers.BooleanField(
        label="是否填充",
        required=False,
        default=True
    )

    class Meta:
        model = models.UserData
        fields = ["cloudword","circle","tag","width","color","full","cloudword_width"]

    def get_cloudword(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.cloudword

    def get_cloudword_width(self,obj):

        return obj.cloudword_width

    def update(self, instance, validated_data):

        cloudword_base64 = self.create_cloudword_base64(
            circle=True if validated_data.get("circle") == True else False,
            width=validated_data.get("width", 300),
            tag=validated_data.get("tag", '["Python"]'),
            color=validated_data.get("color", 'rgba(255,255,255,1)'),
            full=True if validated_data.get("full") == True else False,
        )

        instance.cloudword = cloudword_base64  # 赋值 云词图base64
        instance.cloudword_width = validated_data.get("width", "260")  # 赋值 云词图 宽度
        instance.tag = validated_data.get("tag", '["Python"]')  # 赋值 标签
        instance.save()

        return instance







