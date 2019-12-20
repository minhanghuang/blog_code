from rest_framework import serializers
from app.utils.common.files.file import FileBase
from app.utils.common.serializers.serializer import MySerializerBase

from app.utils.common.exceptions import exception
from app_user import models


class UpdateAvatarSerializer(MySerializerBase):
    """更新用户头像-序列化"""

    avatar = serializers.SerializerMethodField(
        label="图片路径",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.UserProfile
        fields = ["avatar",]

    def get_avatar(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.avatar

    def create(self, validated_data):

        data = self.context["request"].data
        user = self.context["request"].user
        file = data.get("file", None)  # 获取前端传过来的图片数据流
        if not file:  # 图片为空
            raise exception.myException400({
                "success": False,
                "msg": "保存失败,后端没拿到图片",
                "results": "",
            })
        else:  # 图片不为空
            base64_data = FileBase.image_to_base64(file)
            user.avatar = base64_data  # 更新图片
            user.save()  # 保存实例

        return user





