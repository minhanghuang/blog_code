from .base.base_sql import MyBaseSqlPyScript
from .blog_test import MyTerminal
import requests


class MySqlClass(MyBaseSqlPyScript):

    def __init__(self, **payload):
        MyBaseSqlPyScript.__init__(self, **payload)

    def do_test(self):

        if self.sql_state in ["start"]: # sql 状态
            self.init_db()  # 初始化数据库
            self.del_db_migrations_files()  # 删除数据库迁移文件
            self.create_db_models()  # 生成数据库模型
            self.copy_sql_files()  # 拷贝.sql文件到数据库中
            self.close_db()  # 关闭链接

        if self.web_state in ["start","stop","restart"] :  # web 状态
            self.start_thread_web_server() # 打开 web服务器

        if self.sql_state in ["start"]: # sql 状态, 是否初始化用户信息
            self.flush_all_redis() # 清空redis
            self.requests_init_user_data() # 给Django发送http请求, 初始化用户信息

        return None

    def do_test0(self):
        self.requests_init_user_data()
        return None

    def do_exit(self):

        if self.sql_state in ["start"]:  # sql 状态
            system_msg = {
                "服务路径": self.project_path,
                "系统版本": self.sys_version,
                "数据库 ip  ": self.sql_ip,
                "数据库 用户 ": self.sql_user,
                "数据库 密码 ": self.sql_password,
                "数据库 名   ": self.sql_db_name,
            }
            self.output_system(**system_msg)

        return None

    def start_thread_web_server(self):
        """
        开启 uwsgi & Nginx 子线程
        :return: None
        """

        self.output_msg("web服务子线程启动", "OK")
        terminal = MyTerminal(**self.payload)  # 打开另一个子线程 - 启动 uwsgi & Nginx
        terminal.setName("web服务自动化-线程2")  # 子线程开始
        terminal.start()  # 子线程开始
        terminal.join()  # 等待 terminal线程 结束

        return None

    def requests_init_user_data(self):
        """
        发送http请求, 初始化用户信息
        :return: None
        """
        ip = "http://{}:{}/api/app/init/".format(self.nginx_server_name, self.nginx_listen)
        password = input("请输入用户密码:")
        ret = requests.post(
            url=ip,
            data={
                "password": password,
            }
        )
        if ret.status_code == 200:
            self.output_msg("请求Api","OK-{}".format(ret.status_code))
        else:
            self.output_msg("请求Api", "失败-{}".format(ret.status_code))

        return None












