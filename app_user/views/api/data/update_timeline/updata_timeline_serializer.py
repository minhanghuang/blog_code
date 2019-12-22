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

    # def create(self, validated_data):
    #     """"""
    #     data_list = models.UserData.objects.filter(id=1)
    #     if not data_list.exists(): # 如果id=1的数据不存在, 新建
    #         data_obj = models.UserData.objects.create(
    #             id = 1,
    #             tag = '["Python"]',
    #             cloudword_width = "260",
    #             timeline = validated_data.get("timeline",""),
    #         )
    #     else:
    #         data_obj = data_list.first()
    #
    #     data_obj.timeline = validated_data.get("timeline") # 赋值 云词图 宽度
    #     data_obj.save()
    #
    #     return data_obj

    def update(self, instance, validated_data):

        instance.timeline = validated_data.get("timeline")  # 赋值 云词图 宽度
        instance.save()

        return instance










