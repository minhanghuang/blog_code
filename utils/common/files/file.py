import base64


class FileBase(object):
    """处理文件的基类"""

    @classmethod
    def image_to_base64(cls,file_handle):
        """
        将图片转成base64
        :param file_handle: 文件句柄
        :return: base64
        """
        if file_handle:
            base64_data = base64.b64encode(file_handle.read()).decode()
        else:
            base64_data = None

        return base64_data # 'data:image/jpeg;base64,%s' % base64_data

