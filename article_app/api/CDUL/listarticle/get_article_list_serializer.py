from article_app import models
from rest_framework import serializers
from utils.common.serializers.serializer import MySerializerBase



"""
1. 获取博文列表 序列化
"""
class GetArticleListSerializerCls(MySerializerBase):
    username = serializers.CharField(source="user.username",label="用户名")
    starttime = serializers.SerializerMethodField(label="创建时间")

    class Meta:
        model = models.Article
        fields = [
            "id",
            "username",
            "title",
            "content",
            "starttime",
            "tag",
            "titleimage",
            "pageviews",
        ]

    def get_starttime(self, obj):
        """时间格式化"""
        return self.get_data(date=obj.starttime, detail=False)





