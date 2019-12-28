from app.utils.common.serializers.serializer import MySerializerBase
from app_test import models


class ListTestSerializer(MySerializerBase):
    """查看列表-序列化"""

    class Meta:
        model = models.TestModel
        fields = ["dog",]






