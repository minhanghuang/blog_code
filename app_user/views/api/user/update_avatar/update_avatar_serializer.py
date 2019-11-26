from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase
from utils.common.exceptions import exception
from utils.common.files.file import FileBase




class UpdateAvatarSerializer(MySerializerBase):
    """更新用户头像-序列化"""

    class Meta:
        model = models.UserProfile
        fields = []
        # fields = ["username","email","role","description","company","department","position","city","tags","avatar",]
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





