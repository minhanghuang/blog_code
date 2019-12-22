from rest_framework import serializers
from app.utils.common.serializers.serializer import MySerializerBase
from app_user import models


class UpdateTimeLineSerializer(MySerializerBase):
    """更新时光轴-序列化"""

    timeline = serializers.CharField(
        label="时光轴",
        required=True,
    )

    class Meta:
        model = models.UserData
        fields = ["timeline",]

    def update(self, instance, validated_data):

        print("validated_data:",validated_data,type(validated_data))
        instance.timeline = validated_data.get("timeline")  # 赋值 云词图 宽度
        instance.save()

        return instance










