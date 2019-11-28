from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase




class UpdateUserSerializer(MySerializerBase):
    """更新用户详细信息-序列化"""

    avatar = serializers.SerializerMethodField(
        label="图片路径",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.UserProfile
        fields = ["name","email","description","company","department","position","city","tag","avatar",]
        extra_kwargs = {
            'avatar': {
                'allow_null': True,
                'allow_blank': True,
                'required': False,
            },
        }

    def get_avatar(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.avatar

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.email = validated_data.get("email")
        instance.company = validated_data.get("company")
        instance.department = validated_data.get("department")
        instance.position = validated_data.get("position")
        instance.city = validated_data.get("city")
        instance.tag = validated_data.get("tag")
        instance.save()

        return instance





