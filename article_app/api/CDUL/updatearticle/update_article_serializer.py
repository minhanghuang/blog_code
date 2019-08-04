from article_app import models
from rest_framework import serializers
from utils.common.serializers.serializer import MySerializerBase
from utils.common.serializers.serializer import error_instance



"""
1. 修改博文信息 序列化
"""
class UpdateArticleSerializerCls(MySerializerBase):
    title = serializers.CharField(
        label="标题",
        help_text="标题",
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages=error_instance.field_errormsg(field="标题")
    )
    content = serializers.CharField(
        label="内容",
        help_text="内容",
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages=error_instance.field_errormsg(field="内容")
    )

    class Meta:
        model = models.Article
        fields = ["title", "content", ]

    def update(self, instance, validated_data):
        title = validated_data.get("title","")
        content = validated_data.get("content","")


        models.Article.objects.update(
            title=title,
            content = content
        )


        return instance





