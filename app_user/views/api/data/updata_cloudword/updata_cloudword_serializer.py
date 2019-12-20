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
        """
        生成Data数据
        无论Data里面数据的id是多少,总是选择id=1的数据进行修改/新增
        不存在id=1的数据就新增, 存在就修改
        仅仅涉及 id tag cloudword_width cloudword 这四个字段
        其他字段, 单独新增接口操作
        :param validated_data:
        :return:
        """
        cloudword_base64 = self.create_cloudword_base64(
            circle = True if validated_data.get("circle")=="true" else False,
            width = validated_data.get("width", 300),
            tag = validated_data.get("tag", '["Python"]'),
            color = validated_data.get("color", 'rgba(255,255,255,1)'),
            full = True if validated_data.get("full")=="true" else False,
        )
        data_list = models.UserData.objects.filter(id=1)
        if not data_list.exists(): # 如果id=1的数据不存在, 新建
            data_obj = models.UserData.objects.create(
                id = 1,
                tag = validated_data.get("tag",'["Python"]'),
                cloudword_width = validated_data.get("width","260"),
            )
        else:
            data_obj = data_list.first()

        data_obj.cloudword = cloudword_base64 # 赋值 云词图base64
        data_obj.cloudword_width = validated_data.get("width","260") # 赋值 云词图 宽度
        data_obj.tag = validated_data.get("tag",'["Python"]') # 赋值 标签
        data_obj.save()

        return data_obj







