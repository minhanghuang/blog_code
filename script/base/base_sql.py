from .base import MyBasePyScript
import MySQLdb
import platform
import os


SQL_DATA = {
    "Darwin":{
        "db_data":{
            "ip":"127.0.0.1",
            "user":"root",
            "password":"root",
            "db_name":"blog_db",
        }
    },
    "Linux":{
        "db_data":{
            "ip":"127.0.0.1",
            "user":"root",
            "password":"root",
            "db_name":"blog_db",
        }
    },
    "Windows":{
        "db_data":{
            "ip":"127.0.0.1",
            "user":"root",
            "password":"root",
            "db_name":"blog_db",
        }
    }
}


class MyBaseSqlPyScript(MyBasePyScript):


    def __init__(self, **payload):
        MyBasePyScript.__init__(self, **payload)

    def run(self):

        self.do_init()
        self.do_test()
        self.do_exit()

    def do_init(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$ 线程已开启 $$$$$$$$$$$$$$$$$$$$$$$$$")
        self.get_sql_data() # 根据系统的不同, 设置不同的属性
        self.set_sql_path() # 配置路径
        self.init_db() # 初始化数据库

        return None

    def set_sql_path(self):

        self.script_path = os.path.abspath('.')  # script 绝对路径
        self.project_path = self.script_path.split("script")[0]  # server 绝对路径

        return None

    def get_sql_data(self):
        """
        根据系统的不同, 设置不同的属性
        :return: None
        """
        self.sys_version = platform.uname().system  # 系统版本 Darwin Linux
        self.sql_ip = SQL_DATA.get(self.sys_version).get("db_data")["ip"]
        self.sql_user = SQL_DATA.get(self.sys_version).get("db_data")["user"]
        self.sql_password = SQL_DATA.get(self.sys_version).get("db_data")["password"]
        self.sql_db_name = SQL_DATA.get(self.sys_version).get("db_data")["db_name"]

        return None

    def del_db_migrations_files(self):
        """
        删除数据库迁移文件
        :return: None
        """

        for maindir, subdir, file_name_list in os.walk(self.project_path):
            if "migrations" in maindir and "__pycache__" not in maindir:
                for filename in file_name_list:
                    if "__init__.py" != filename:
                        initial_path = os.path.join(maindir, filename)  # 合并成一个完整路径
                        os.remove(initial_path) # 删除
        print("==== 数据库: 迁移文件已删除")

        return None

    def create_db_models(self):
        """
        生成数据库模型
        :return: None
        """

        self.set_command_group(["{} {}manage.py makemigrations".format(self.python_evn, self.project_path)], "makemigrations")
        self.set_command_group(["{} {}manage.py migrate".format(self.python_evn, self.project_path)], "migrate")
        print("==== 数据库: Models已生成")

        return None

    def init_db(self):
        self.del_db_migrations_files() # 删除数据库迁移文件
        self.create_db_models() # 生成数据库模型
        # try:
        #     db = MySQLdb.connect(
        #         self.sql_ip,
        #         self.sql_user,
        #         self.sql_password,
        #         self.sql_db_name,
        #         charset='utf8'
        #     )
        # except Exception as e:
        #     print(e)