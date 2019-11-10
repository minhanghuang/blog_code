from rest_framework import serializers
from app_article import models
from utils.common.serializers.serializer import MySerializerBase




class CreateTestSerializer(MySerializerBase):
    """新增测试-序列化"""

    count = serializers.IntegerField()
    class Meta:
        model = models.Article
        fields = ["count",]

    def create(self, validated_data):

        user = self.context["request"].user # 登录用户
        image = self.context["request"].data.get("file",None)

        for foo in range(int(validated_data["count"])):
            article_obj = models.Article.objects.create(
                author = user,
                title = self.get_fake_obj().sentence(),
                content = self.get_fake_obj().text(),
                image = image,

            )
        article_obj = models.Article.objects.create(
            author=user,
            title=self.get_fake_obj().sentence(),
            content=self.get_fake_obj().text(),
            image=image,
        )
        return article_obj







