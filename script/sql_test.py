from base.base_sql import MyBaseSqlPyScript


class MySqlClass(MyBaseSqlPyScript):

    def __init__(self, **payload):
        MyBaseSqlPyScript.__init__(self, **payload)

    def do_test(self):

        return None

    def do_exit(self):
        print("++++ Sql信息 +++++++++++++++++++++++++++++++++++++++++")
        print("++++ 服务路径: {}".format(self.project_path))
        print("++++ 系统版本: {}".format(self.sys_version))
        print("++++ 数据库 ip   : {}".format(self.sql_ip))
        print("++++ 数据库 用户 : {}".format(self.sql_user))
        print("++++ 数据库 密码 : {}".format(self.sql_password))
        print("++++ 数据库 名   : {}".format(self.sql_db_name))

        print("$$$$$$$$$$$$$$$$$$$$$$$$$ 线程已结束 $$$$$$$$$$$$$$$$$$$$$$$$$")

        return None











