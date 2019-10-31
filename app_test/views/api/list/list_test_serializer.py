from rest_framework import serializers
from app_test import models
from utils.common.serializers.serializer import MySerializerBase




class ListTestSerializer(MySerializerBase):
    """查看列表-序列化"""

    class Meta:
        model = models.TestModel
        fields = ["dog",]






