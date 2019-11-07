from app_article import models
from utils.common.serializers.serializer import MySerializerBase




class CreateArticleSerializer(MySerializerBase):
    """新增博文-序列化"""

    class Meta:
        model = models.Article
        fields = ["title","content",]

    def create(self, validated_data):
        user = self.context["request"].user # 登录用户
        article_obj = models.Article.objects.create(
            author = user,
            title = validated_data["title"],
            content = validated_data["content"],
        )

        return article_obj





