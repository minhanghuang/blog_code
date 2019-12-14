from django.test import TestCase

# Create your tests here.


# import time
#
#
# def upload_images_path(instance, filename):
#
#     last = filename.split(".")[1]
#
#     return "images/blog/{}.{}".format(str(int(time.time() * 1000000)),last)
#
# print(upload_images_path("","njjbjkn.jpg"))

# import random
#
# print(random.randint(1,2))

import jieba

from wordcloud import WordCloud

# with open("word.txt") as fp:
#     txt = fp.read()  # 读取文本
#
# words = jieba.lcut(txt)  # 精确分词
#
# nextword = ''.join(words)  # 空格连接字符
#
# print(nextword)
import numpy as np
x, y = np.ogrid[:600, :600]

mask = (x - 300) ** 2 + (y - 300) ** 2 > 300 ** 2
mask = 255 * mask.astype(int)
print(mask)
text = "Python Python Django Vue Vue Nginx Apache  iView Element RabbitMQ Redis MySQL Scrapy Mac CentOS JavaScript MongoDB C/C++ webSocket ARM STM32 NPN "
wordshow = WordCloud(background_color='white',
                     # width=500,
                     # height=500,
                     # max_words=50,
                     # max_font_size=100,
                    repeat=True,
                    mask=mask,
                     font_path='/System/Library/Fonts/Monaco.dfont',  # 用微软雅黑作为字体显示效果
                     ).generate(text)

wordshow.to_file('tes4.png')  # 转换成图片
