from base.base_sql import MyBaseSqlPyScript


class MySqlClass(MyBaseSqlPyScript):

    def __init__(self, **payload):
        MyBaseSqlPyScript.__init__(self, **payload)


    def do_test(self):

        return None

    def do_exit(self):
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











