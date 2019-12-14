from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase
from utils.common.exceptions import exception
from utils.common.files.file import FileBase




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
    circle = serializers.CharField(
        label="图片形状(True:圆形,False:正方形)",
        required=False,
        allow_null=True,
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
    full = serializers.CharField(
        label="是否填充",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.UserData
        fields = ["cloudword","circle","tag","width","color","full","cloudword_width"]

    def get_cloudword(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.cloudword

    def get_cloudword_width(self,obj):

        return obj.cloudword_width

    def create(self, validated_data):

        cloudword_base64 = self.create_cloudword_base64(
            circle = validated_data.get("circle", True),
            width = validated_data.get("width", 300),
            tag = validated_data.get("tag", '["Python"]'),
            color = validated_data.get("color", 'rgba(255,255,255,1)'),
            full = validated_data.get("full", True),
        )
        data_list = models.UserData.objects.filter(id=1)
        if not data_list.exists(): # 如果id=1的数据不存在, 新建
            data_obj = models.UserData.objects.create(
                id = 1,
                tag = validated_data.get("tag",'["Python"]'),
                width = validated_data.get("width","260"),
            )
        else:
            data_obj = data_list.first()

        data_obj.cloudword = cloudword_base64
        data_obj.cloudword_width = validated_data.get("width","260")
        data_obj.tag = validated_data.get("tag",'["Python"]')
        data_obj.save()

        return data_obj







