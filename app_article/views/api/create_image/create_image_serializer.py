from app_article import models
from utils.common.serializers.serializer import MySerializerBase
from utils.common.exceptions import exception




class CreateImageSerializer(MySerializerBase):
    """新增图片-序列化"""

    class Meta:
        model = models.Image
        fields = []

    def create(self, validated_data):
        """
        提价图片:1.图片已经存在->更新图片;2.图片不存在->2.1文章不存在->报错;2.2文章存在->新建图片
        :param validated_data:
        :return:
        """
        data = self.context["request"].data # 前端拿到的数据 (文件流,文章id)
        print(data.get("id"))
        print(data.get("file"))
        article_list = models.Article.objects.filter(
            id=data.get("id")
        ) # 文章列表
        if not article_list.exists(): # 文章不存在
            raise exception.myException401({
                "success": False,
                "msg": "文章不存在",
                "results": "",
            })

        article_obj = article_list.first() # 文章对象
        image_list = models.Image.objects.filter(
            article = article_obj
        ) # 图片列表
        if not image_list.exists(): # 图片不存在 -> 提交图片
            image_obj = models.Image.objects.create(
                article = article_obj,
                image = data.get("file",None),
            )
        else: # 图片存在 -> 更新图片
            image_obj = models.Image.objects.update(
                image=data.get("file", None),
            )

        return image_obj





