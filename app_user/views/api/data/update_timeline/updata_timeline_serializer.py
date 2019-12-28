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

        value = validated_data.get("timeline", {})
        value = eval(value)

        for index, foo in enumerate(value):
            foo["id"] = str(index)

        instance.timeline = str(value).replace("'","\"")
        # 后端存储单引号, 前端JSON.parse()的时候,不能识别单引号, 需要在后端存储数据的时候处理,
        # 因为在前面几行代码,做了强制类型转化,Python会将双引号转成单引号,如果没有做强制类型转换,直接保存前端传来的字符串,没这个问题
        instance.save()

        return instance










