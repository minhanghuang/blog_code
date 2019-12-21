import platform
from basedata.target.initdata import init_data


class MyConfig(object):
    """
    配置 本地调试环境 / 生产环境
    """

    def __init__(self, evn="dev"):
        """
        初始化
        :param evn: dev-本地调试环境; prod-生产环境
        """
        self.get_system_info()
        self.get_system_ttf()
        if evn=="dev": # 本地调试环境
            self.DEBUG = True # 是否允许debug
            self.APIDOCSROUTER = True # 是否允许打开Api文档路由
        else:
            self.DEBUG = False # 是否允许debug
            self.APIDOCSROUTER = False # 是否允许打开Api文档路由


    def get_system_info(self):
        """
        获取本地服务器系统信息
        :return: None
        """
        self.SYSVERSION = platform.uname().system # 系统类型 macOS-Darwin; linux-Linux; other

        return None

    def get_system_ttf(self):
        """
        获取系统字体路径
        :return: None
        """

        if self.SYSVERSION == "Darwin": # Mac
            # self.FONTPATH = "/System/Library/Fonts/Monaco.dfont" # 不支持中文
            self.FONTPATH = init_data["ttf"]["Mac"]

        elif self.SYSVERSION == "Linux": # Linux
            # self.FONTPATH = "/usr/share/fonts/windows/msyh.ttf" # 支持中文
            self.FONTPATH = init_data["ttf"]["Linux"]

        else: # Windows
            # self.FONTPATH = "C:/Windows/Fonts/STFANGSO.ttf"
            self.FONTPATH = init_data["ttf"]["Windows"]

        return None

    def get_redis_config(self):

        redis_dict = {}
        redis_dict["host"] = init_data["redis"]["basedb"]["host"]
        redis_dict["port"] = init_data["redis"]["basedb"]["port"]
        redis_dict["db"] = init_data["redis"]["basedb"]["db"]

        return redis_dict

    def get_celery_config(self):
        """
        获取celery配置文件
        :return: dict
        """

        return init_data["celery"]



myconfig = MyConfig(
    evn="dev", # dev-本地调试环境; prod-生产环境
)


if __name__ == "__main__":

    print("__main__")
