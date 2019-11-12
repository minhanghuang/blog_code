from app_article import models
from utils.common.serializers.serializer import MySerializerBase
from rest_framework import serializers




class UpdateArticleSerializer(MySerializerBase):
    """更新博文-序列化"""

    image = serializers.SerializerMethodField(
        label="图片",
    )
    statetype = serializers.SerializerMethodField(
        label="请求类型,保存草稿箱--0 Or 发布文章(更新文章/发布新文章)--1",
        required=True,
    )
    class Meta:
        model = models.Article
        fields = ["statetype","title","subtitle","content","state","image",]

    def update(self, instance, validated_data):
        """
        逻辑: 首先判断参数中的id是否正常(正数:正常,负数和0:异常)
            异常的id: 直接抛401
            正常的id: 在Article中查看id是否已经存在
                存在: 更新Article -- title:title, subtitle: subtitle, content: content, statue: 0,
        :param instance:
        :param validated_data:
        :return:
        """


        return instance





