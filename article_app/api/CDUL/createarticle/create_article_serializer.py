from article_app import models
from rest_framework import serializers
from utils.common.serializers.serializer import error_instance
from utils.common.serializers.serializer import MySerializerBase




"""
1. 新增博文 序列化
"""
class CreateArticleSerializerCls(MySerializerBase):
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
        fields = ["title","content",]
        # extra_kwargs = {
        #     'username': {'allow_null': True},
        #     'password': {'allow_null': True},
        # }

    def validate_content(self, content):
        """自定义校验content"""
        return content

    def create(self, validated_data):
        title = validated_data.get("title","")
        content = validated_data.get("content","")
        user = self.context["request"].user
        article_obj = models.Article.objects.create(
            user = user,
            title=title,
            content = content,
        )

        return article_obj



