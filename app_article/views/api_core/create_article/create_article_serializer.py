from app.utils.common.serializers.serializer import MySerializerBase
from app_article import models


class CreateArticleSerializer(MySerializerBase):
    """新增博文-序列化"""

    class Meta:
        model = models.Article
        fields = ["id","title","content","state"]

    def create(self, validated_data):

        user = self.context["request"].user # 登录用户
        article_obj = models.Article.objects.create(
            author = user,
            title = validated_data.get("title",None),
            content = validated_data.get("content",""),
            state = validated_data.get("state",0), # 0:草稿箱,1:公开,2:秘密
        )

        return article_obj





