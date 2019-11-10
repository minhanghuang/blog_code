from rest_framework import serializers
from app_test import models
from utils.common.serializers.serializer import MySerializerBase




class CreateImagSerializer(MySerializerBase):
    """新增测试-序列化"""

    class Meta:
        model = models.TestModel
        fields = ["image",]

    def create(self, validated_data):
        print(self.context["request"].data)
        obj = models.TestModel.objects.create(
            image = self.context["request"].data.get("file",None)
        )

        return obj







