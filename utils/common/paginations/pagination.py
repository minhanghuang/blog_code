from rest_framework.pagination  import PageNumberPagination
from django.conf import settings
from rest_framework.response import Response
from collections import OrderedDict
import math



# 自定义分页类

class MyPagination(PageNumberPagination):
    msg_list = "ok"
    page_size = settings.MY_PAGE_SIZE    # 每页显示多少个
    page_size_query_param = settings.MY_PAGE_SIZE_QUERY_PARAM # 可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    max_page_size = settings.MY_MAX_PAGE_SIZE # 最大页数不超过500
    page_query_param = settings.MY_PAGE_QUERY_PARAM # 获取页码数的

    def get_total_pages(self):
        """总页数"""
        return math.ceil(self.page.paginator.count / self.page_size)  # 向上取整

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('size', self.page_size),
            ('totalpages', self.get_total_pages()),
            ('success', True),
            ('msg', self.msg_list),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
         ]))

