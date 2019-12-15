import platform



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
            self.FONTPATH = "/System/Library/Fonts/Monaco.dfont" # 不支持中文

        elif self.SYSVERSION == "Linux": # Linux
            self.FONTPATH = "/usr/share/fonts/windows/msyh.ttf" # 支持中文

        else: # Windows
            self.FONTPATH = "C:/Windows/Fonts/STFANGSO.ttf"

        return None



myconfig = MyConfig(
    evn="dev", # dev-本地调试环境; prod-生产环境
)