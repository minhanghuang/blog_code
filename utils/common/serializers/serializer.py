from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from faker import Faker
from wordcloud import WordCloud
import numpy as np


fake_obj = Faker(locale='zh_CN') # 生成一个Faker对象(中文),默认不传参数时为英文


class MySerializerBase(DynamicFieldsMixin,serializers.ModelSerializer):


    def create_cloudword_base64(self, circle, width, tag, color, full):
        """
        生成云词图
        :param circle: 是否是圆形
        :param width: 大小
        :param tag: 关键字
        :param color: 背景颜色
        :param full: 是否填充
        :return: 云词图base64
        """

        tag_str = "" # 空格隔开
        tag = eval(tag)
        if isinstance(tag, list):
            for foo in tag:
                tag_str = " ".join((tag_str,foo))

        


        print("tag_str:",tag_str)

        return ""

    def get_fake_obj(self):
        """
        获取fake对象
        :return: fake_obj
        """
        return fake_obj

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

