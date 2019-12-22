# from django.test import TestCase
#
# # Create your tests here.
#
#
# # import time
# #
# #
# # def upload_images_path(instance, filename):
# #
# #     last = filename.split(".")[1]
# #
# #     return "images/blog/{}.{}".format(str(int(time.time() * 1000000)),last)
# #
# # print(upload_images_path("","njjbjkn.jpg"))
#
# # import random
# #
# # print(random.randint(1,2))
#
# import jieba
#
# from wordcloud import WordCloud
#
# # with open("word.txt") as fp:
# #     txt = fp.read()  # 读取文本
# #
# # words = jieba.lcut(txt)  # 精确分词
# #
# # nextword = ''.join(words)  # 空格连接字符
# #
# # print(nextword)
# import numpy as np
# # x, y = np.ogrid[:600, :600]
# #
# # mask = (x - 300) ** 2 + (y - 300) ** 2 > 300 ** 2
# # mask = 255 * mask.astype(int)
# # print(mask)
# # text = "Python Python Django Vue Vue Nginx Apache  iView Element RabbitMQ Redis MySQL Scrapy Mac CentOS JavaScript MongoDB C/C++ webSocket ARM STM32 NPN "
# # wordshow = WordCloud(background_color='rgba(255,255,255,1)',
# #                      width=100,
# #                      height=100,
# #                      # max_words=50,
# #                      # max_font_size=100,
# #                     repeat=True,
# #                     mask=None,
# #                      font_path='/System/Library/Fonts/Monaco.dfont',  # 用微软雅黑作为字体显示效果
# #                      ).generate(text)
# #
# # wordshow.to_file('tes4.png')  # 转换成图片
#
# import platform
#
# print(platform.platform())
# print(platform.uname().system)
a = [
    {"id": "0", "color": "blue", "icon": "md-snow", "count_inner": 1, "content": [
        {"id_inner": "0", "col": "第一次接触编程"},
        {"id_inner": "1", "col": "C语言 Hello World"}], "node_name": "2014/09"},
    {"id": "1", "color": "blue", "icon": "md-ionic", "count_inner": 1, "content": [
        {"id_inner": "0", "col": "大一暑假"},
        {"id_inner": "1", "col": "自学单片机"}], "node_name": "2015/07"},
    {"id": "2", "color": "blue", "icon": "md-ionic", "count_inner": 3, "content": [
        {"id_inner": "0", "col": "大二"},
        {"id_inner": "1", "col": "自学电路,设计PCB电路板"},
        {"id_inner": "2", "col": "基于单片机完成计算器电路的设计,并给计算器编写一套简易的系统"},
        {"id_inner": "3", "col": "完成计算器的成品事物输出"}], "node_name": "2016/02"},
    {"id": "3", "color": "blue", "icon": "md-ionic", "count_inner": 2, "content": [
        {"id_inner": "0", "col": "大二暑假"},
        {"id_inner": "1", "col": "加入老师实验室学习"},
        {"id_inner": "2", "col": "参加全国学生电子设计竞赛"}], "node_name": "2016/07"},
    {"id": "4", "color": "blue", "icon": "md-ionic", "count_inner": 3, "content": [
        {"id_inner": "0", "col": "大三"},
       {"id_inner": "1", "col": "自学ARM"},
       {"id_inner": "2", "col": "负责实验室的机器人项目"},
        {"id_inner": "3", "col": "开发一款小型的四轴飞行器"}], "node_name": "2016/09"},
    {"id": "5", "color": "blue", "icon": "md-ionic", "count_inner": 2, "content": [
        {"id_inner": "0", "col": "大三寒假"},
        {"id_inner": "1", "col": "开始接触Linux"},
        {"id_inner": "2", "col": "开发树莓派,第一次接触Python"}], "node_name": "2017/02"},
    {"id": "6", "color": "blue", "icon": "md-ionic", "count_inner": 3, "content": [
        {"id_inner": "0", "col": "大四"},
        {"id_inner": "1", "col": "自学Python web开发"},
        {"id_inner": "2", "col": "使用Django开发自己的第一个博客网站"},
        {"id_inner": "3", "col": "域名: www.huangminhang.cn"}], "node_name": "2017/10"},
    {"id": "7", "color": "blue", "icon": "md-ionic", "count_inner": 3, "content": [
        {"id_inner": "0", "col": "大四毕业"},
        {"id_inner": "1", "col": "毕业设计:基于Zigbee无线无线温度控制"},
        {"id_inner": "2", "col": "事物布局+电路设计+代码编写+PC端上位机(C#)"},
        {"id_inner": "3", "col": "毕业设计特等奖"}], "node_name": "2018/06"},
    {"id": "8", "color": "blue", "icon": "md-ionic", "count_inner": 2, "content": [
        {"id_inner": "0", "col": "第一份正式的工作"},
        {"id_inner": "1", "col": "使用Django REST Framework开发公司后端接口"},
        {"id_inner": "2", "col": "一个人负责公司多个产品后端接口的开发"}], "node_name": "2018/07"},
    {"id": "9", "color": "blue", "icon": "md-ionic", "count_inner": 1, "content": [
        {"id_inner": "0", "col": "公司产品生产部署"},
        {"id_inner": "1", "col": "Scrapy爬虫的框架的学习"}], "node_name": "2018/12"},
    {"id": "10", "color": "blue", "icon": "md-ionic", "count_inner": 1, "content": [
        {"id_inner": "0", "col": "针对公司产品的流水业务,设计异步统计流水账单的系统"},
        {"id_inner": "1", "col": "Celery & RAbbitMQ"}], "node_name": "2019/03"},
    {"id": "11", "color": "blue", "icon": "md-ionic", "count_inner": 3, "content": [
        {"id_inner": "0", "col": "自学Vue.js"},
        {"id_inner": "1", "col": "两周完成Vue框架的使用"},
        {"id_inner": "2", "col": "搭建个人的第二个博客系统"},
        {"id_inner": "3", "col": "前端:Vue 后端:Django"}], "node_name": "2019/10"},
]
print(a)

a.sort(key=lambda k: (int(k.get('id'))),reverse=True)

print(a)


