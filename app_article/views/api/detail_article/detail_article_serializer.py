from app_article import models
from utils.common.serializers.serializer import MySerializerBase
from rest_framework import serializers




class DetailArticleSerializer(MySerializerBase):
    """查看博文详细-序列化"""

    username = serializers.CharField(
        source="author.username",
        label="作者",
    )
    state = serializers.CharField(
        source="get_state_display",
        label="博文是否可见",
    )
    createdate = serializers.SerializerMethodField(label="创建时间")
    updatedate = serializers.SerializerMethodField(label="修改时间")
    image = serializers.SerializerMethodField(label="图片")

    class Meta:
        model = models.Article
        fields = ["id","username","title","subtitle","content","createdate","updatedate","state","category","tag","istop","image"]

    def get_createdate(self,obj):

        return self.date_to_str(obj.createdate)

    def get_updatedate(self, obj):

        return self.date_to_str(obj.updatedate)

    def get_image(self, obj):

        return 'data:image/jpeg;base64,{}'.format(obj.image)





