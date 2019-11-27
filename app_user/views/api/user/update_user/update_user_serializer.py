from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase




class UpdateUserSerializer(MySerializerBase):
    """更新用户详细信息-序列化"""



    class Meta:
        model = models.UserProfile
        fields = ["username","email","description","company","department","position","city","tag","avatar"]
        extra_kwargs = {
            'username': {
                'allow_null': True,
                'allow_blank': True,
                'required': False,
            },
            'avatar': {
                'allow_null': True,
                'allow_blank': True,
                'required': False,
            },
        }

    def update(self, instance, validated_data):
        instance.description = validated_data.get("description")
        instance.email = validated_data.get("email")
        instance.company = validated_data.get("company")
        instance.department = validated_data.get("department")
        instance.position = validated_data.get("position")
        instance.city = validated_data.get("city")
        instance.tag = validated_data.get("tag")
        instance.save()

        return instance





