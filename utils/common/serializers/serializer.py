from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

class MySerializerBase(DynamicFieldsMixin,serializers.ModelSerializer):

    def date_to_str(self, date, detail=True):
        """
        时间转字符串
        :param date: 时间
        :param detail: 是否显示详细时间
        :return: str_date
        """
        if detail:
            return date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return date.strftime("%Y-%m-%d")

    @classmethod
    def field_error_msg(cls,*args,**kwargs):
        """
        字段错误走这里
        :param args:
        :param kwargs:
        :return: error msg
        """

        field = kwargs.get("field"," ")

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

