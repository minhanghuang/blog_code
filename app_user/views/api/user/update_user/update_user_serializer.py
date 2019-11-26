from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase




class UpdateUserSerializer(MySerializerBase):
    """更新用户详细信息-序列化"""

    class Meta:
        model = models.UserProfile
        fields = []
        # fields = ["username","email","role","description","company","department","position","city","tags","avatar",]

    def update(self, instance, validated_data):



        return instance





