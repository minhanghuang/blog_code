import os
import platform
import sys
from threading import Thread
from configparser import ConfigParser

# TODO
SYSTEM_DATA = {
    "nginx":{
        "Darwin":{
            "nginx_start_cmd":"sudo nginx",
            "nginx_stop_cmd":"sudo nginx -s stop",
            "nginx_restart_cmd":"sudo nginx -s reload",
        },
        "Linux":{
            "nginx_start_cmd":"/etc/init.d/nginx start",
            "nginx_stop_cmd":"/etc/init.d/nginx stop",
            "nginx_restart_cmd":"/etc/init.d/nginx restart",
        },
        "Windows":{
            "nginx_start_cmd":"",
            "nginx_stop_cmd":"",
            "nginx_restart_cmd":"",
        },
    },
    "http":{
        "Darwin":{
            "http":"127.0.0.1:19900",
        },
        "Linux":{
            "http": "api.minhung.me:19900",
        },
        "Windows":{
            "http": "127.0.0.1:19900",
        },
    },
}

class MyBasePyScripy(Thread):

    def __init__(self,  **payload):
        Thread.__init__(self)

        self.state = payload.get("state", "pass")
        self.server_name = payload.get("server_name", "blog_code")

    def run(self):
        self.do_init() # 初始化
        self.do_test() # 测试单元
        self.do_exit() # 退出

    def do_exit(self):
        print("==== 系统: {} ".format(self.sys_version))
        print("==== server: {} ".format(self.http))
        print("==== 服务名: {} ".format(self.server_name))
        print("==== 服务路径: {} ".format(self.project_path))
        print("==== 脚本路径: {} ".format(self.script_path))
        print("==== uwsgi路径: {} ".format(self.uwsgi_path))
        print("======== uwsgi.ini 路径: {} ".format(self.uwsgi_ini_path))
        print("======== uwsgi.sock 路径: {} ".format(self.uwsgi_sock_path))
        print("======== uwsgi.log 路径: {} ".format(self.uwsgi_log_path))
        print("======== uwsgi.pid 路径: {} ".format(self.uwsgi_pid_path))
        print("==== nginx路径: {} ".format(self.nginx_path))
        return None

    def do_test(self):
        """
        执行单元
        :return: None
        """

        print("基类的do_test")

        return None

    def do_init(self):
        """
        基类自定义初始化
        :return:
        """

        self.set_sys_data() # 根据系统的不一样, 设置不同的信息
        self.set_path() # 设置路径

        return None

    def set_sys_data(self):
        """
        根据不同的系统,配置不同的信息
        :return: None
        """
        self.sys_version = platform.uname().system  # 系统版本 Darwin Linux

        nginx_data = SYSTEM_DATA.get("nginx").get(self.sys_version)
        self.nginx_start_cmd = nginx_data.get("nginx_start_cmd")
        self.nginx_stop_cmd = nginx_data.get("nginx_stop_cmd")
        self.nginx_restart_cmd = nginx_data.get("nginx_restart_cmd")

        http_data = SYSTEM_DATA.get("http").get(self.sys_version)
        self.http = http_data.get("http") # 设置 ip:port

        return None

    def set(self, command):

        print("正在发送命令: {}".format(command))

        return os.system(command)

    def set_command_group(self, command_list):
        """
        设置命令 - 多条
        :param command_list:
        :return: None
        """
        if isinstance(command_list,list):
            for foo in command_list:
                self.set_command(foo)
        else:
            pass

        return None

    def set_command(self, command="pwd"):
        """
        设置命令 - 单条
        :param command: 命令
        :return: ret
        """

        return self.set(command)

    def set_path(self):
        """
        获取项目路径
        :return: None
        """
        self.script_path = os.path.abspath('.') # script 绝对路径
        self.project_path = self.script_path.split("script")[0] # server 绝对路径

        self.uwsgi_path = self.script_path + "/app_sh/uwsgi" # uwsgi 绝对路径
        self.uwsgi_ini_path = self.script_path + "/app_sh/uwsgi/uwsgi.ini" # uwsgi.ini 绝对路径
        self.uwsgi_pid_path = self.script_path + "/app_sh/uwsgi/uwsgi.pid" # uwsgi.pid 绝对路径
        self.uwsgi_log_path = self.script_path + "/app_sh/uwsgi/uwsgi.log" # uwsgi.log 绝对路径
        self.uwsgi_sock_path = self.script_path + "/app_sh/uwsgi/uwsgi.sock" # uwsgi.sock 绝对路径


        self.nginx_path = self.script_path + "/app_sh/nginx" # nginx绝对路径

        return None

    def kill_pid(self, pid_list):
        """

        :param pid_list: 进程pid列表
        :return: None
        """
        if isinstance(pid_list,list):
            for foo in pid_list:
                self.set_command("sudo kill -9 {}".format(foo))
        else:
            pass

        return None


    def get_uwsgi_pid(self):
        """
        获取uwsgi进程的id
        :return: list
        """

        ret_list = []
        out = os.popen("ps -ef | grep uwsgi").read()
        for line in out.splitlines():
            ret_list.append(line.split()[1])


        return ret_list

    def get_nginx_pid(self):
        """
        获取nginx进程的id
        :return: list
        """

        ret_list = []
        out = os.popen("ps -ef | grep nginx").read()
        for line in out.splitlines():
            ret_list.append(line.split()[1])

        return ret_list

    def create_uwsgi_ini_file(self):
        """生成uwsgi.ini文件"""

        self.set_uwsgi_ini(self.uwsgi_ini_path, "chdir", self.project_path) # 服务路径
        self.set_uwsgi_ini(self.uwsgi_ini_path, "module", self.server_name+".wsgi:application") # 服务名
        self.set_uwsgi_ini(self.uwsgi_ini_path, "socket", self.uwsgi_sock_path) # sock路径
        self.set_uwsgi_ini(self.uwsgi_ini_path, "pidfile", self.uwsgi_pid_path) # pid文件 路径
        self.set_uwsgi_ini(self.uwsgi_ini_path, "daemonize", self.uwsgi_log_path) # ip:port
        self.set_uwsgi_ini(self.uwsgi_ini_path, "http", self.http) # ip:port

        return None

    def has_file_exists(self, file_path, data=""):
        """
        判断文件是否存在,
        :param file_path: 文件路径
        :param data: 数据
        :return: None
        """

        ret_path = os.path.isfile(file_path)
        if ret_path: # 文件存在

            pass

        else: # 文件不存在
            pass

        return None

    def read_ini(self, file_path, out_key, inner_key):
        """
        读ini文件
        :param file_path: ini文件路径
        :param key: 大键
        :param value: 小键
        :return: 数据
        """

        config = ConfigParser()
        config.read(file_path)
        value = config.get(out_key, inner_key)

        return value

    def read_uwsgi_ini(self,file_path, key):
        """
        读取uwsgi文件的内容
        :param file_path: uwsgi.ini文件路径
        :param key: 键
        :return: 值
        """

        value = self.read_ini(file_path=file_path, out_key="uwsgi", inner_key=key)

        return value

    def set_ini(self, file_path, out_key, inner_key, value=""):
        """
        判断文件是否存在,
        :param file_path: 文件路径
        :param data: 数据
        :return: None
        """

        config = ConfigParser()
        config.read(file_path)
        config.set(out_key, inner_key, value)
        config.write(open(file_path, "r+", encoding="utf-8"))

        return None

    def set_uwsgi_ini(self, file_path, key, value):
        """
        修改uwsgi文件的内容
        :param file_path: uwsgi.ini文件路径
        :param key: 键
        :return: None
        """

        self.set_ini(file_path=file_path, out_key="uwsgi", inner_key=key, value=value)

        return None

