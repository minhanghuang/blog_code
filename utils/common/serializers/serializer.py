from utils.common.exceptions import exception
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

class MySerializer(DynamicFieldsMixin,serializers.ModelSerializer):

    pass

class SerializerPlug(object):
    """
    自定义序列化异常
    """
    def __init__(self):
        self.msg_error = "error"
        self.msg_detail = "field"

    def field_errormsg(self,*args,**kwargs):
        """
        字段错误走这里
        :param args:
        :param kwargs:
        :return: error msg
        """

        field = kwargs.get("field","")

        return {
            "unique": "{}已经被注册。".format(field),
            "required": "{}不能为空。".format(field),
            "min_length": "%s长度不能小于{min_length}。" % field,
            "max_length": "%s长度不能大于{max_length}。" % field,
            "max_value": "确保%s小于或等于{max_value}。" % field,
            "min_value": "确保%s大于或等于{min_value}。" % field,
            "max_digits": "确保%s总共不超过{max_digits}个数字。" % field,
            'invalid': "{}不合法。".format(field),
            'blank': "{}不可以是空白。".format(field),
            'max_string_length': "{}值太大。".format(field),
            'max_whole_digits': "确保%s小数位数不超过{max_decimal_places}。" % field,
            'max_decimal_places': "确保%s小数点前不超过{max_whole_digits}个数字。" % field,
            'overflow': "{}日期时间值超出范围。".format(field),
        }

    def validation_error(self, serializer):
        """
        序列化错误走这里
        drf的异常处理不能满足需求
        """
        try:
            serializer.is_valid(raise_exception=True) # 捕获异常
        except Exception as e:
            print(e)
            dict_exception = e.__dict__
            for i, k in dict_exception["detail"].items():
                self.msg_detail = i
                self.msg_error = k[0]
                break
            raise exception.myException400({
                "success": False,
                "msg": "{}".format(self.msg_error),
            })
        return None


error_instance = SerializerPlug()



