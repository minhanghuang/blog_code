from app.utils.common.serializers.serializer import MySerializerBase
from app_article import models


class GetStateArticleSerializer(MySerializerBase):
    """查看博文列表-序列化"""

    class Meta:
        model = models.Article
        fields = ["state",]





