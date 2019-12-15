



class MyConfig(object):
    """
    配置 本地调试环境 / 生产环境
    """

    def __init__(self, evn="dev"):
        """
        初始化
        :param evn: dev-本地调试环境; prod-生产环境
        """

        if evn=="dev": # 本地调试环境
            self.DEBUG = True # 是否允许debug
            self.APIDOCSROUTER = True # 是否允许打开Api文档路由
        else:
            self.DEBUG = False # 是否允许debug
            self.APIDOCSROUTER = False # 是否允许打开Api文档路由

    def get_system_ttf(self,):


        return



myconfig = MyConfig(
    evn="dev", # dev-本地调试环境; prod-生产环境
)