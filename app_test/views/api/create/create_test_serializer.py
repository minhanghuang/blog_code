from rest_framework import serializers
from app_test import models
from utils.common.serializers.serializer import MySerializerBase




class CreateTestSerializer(MySerializerBase):
    """新增测试-序列化"""

    class Meta:
        model = models.TestModel
        fields = ["dog",]







