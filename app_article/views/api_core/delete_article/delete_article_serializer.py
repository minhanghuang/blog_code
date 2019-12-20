from app.utils.common.serializers.serializer import MySerializerBase
from app_article import models


class DeleteArticleSerializer(MySerializerBase):
    """删除博文-序列化"""

    class Meta:
        model = models.Article
        fields = ["state"]
        extra_kwargs = {
            'state': {
                'allow_null': False,
                'allow_blank': False,
                'required': True,
            },
        }

    def update(self, instance, validated_data):
        print("validated_data:",validated_data)
        instance.state = validated_data.get("state",3) # 将文章状态改为 3:已删除, 0:草稿箱
        instance.save()

        return instance


