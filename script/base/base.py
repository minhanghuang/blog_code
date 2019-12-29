import os
import re
import platform
from threading import Thread
from configparser import ConfigParser

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
    "uwsgi_http":{
        "Darwin":{
            "http":"127.0.0.1:19900",
        },
        "Linux":{
            "http": "0.0.0.0:19900", # 部署到服务器上之后, uwsgi的ip必须是0.0.0.0
        },
        "Windows":{
            "http": "127.0.0.1:19900",
        },
    },
    "nginx_http":{
        "Darwin":{
            "listen":"19800",
            "server_name":"localhost",
        },
        "Linux":{
            "listen":"19800",
            "server_name":"api.minhung.me", # 如果服务器已经被域名解析,必须填域名
        },
        "Windows":{
            "listen":"19800",
            "server_name":"localhost",
        },
    },
}

class MyBasePyScript(Thread):

    def __init__(self,  **payload):
        Thread.__init__(self)

        self.state = payload.get("state", "pass")
        self.server_name = payload.get("server_name", "blog_code")
        self.python_evn = payload.get("python_evn", "python3")

    def run(self):

        self.do_init() # 初始化
        self.do_test() # 测试单元
        self.do_exit() # 退出

    def do_exit(self):

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

        nginx_http_data = SYSTEM_DATA.get("nginx_http").get(self.sys_version)
        self.nginx_listen = nginx_http_data.get("listen")
        self.nginx_server_name = nginx_http_data.get("server_name")

        http_data = SYSTEM_DATA.get("uwsgi_http").get(self.sys_version)
        self.uwsgi_http = http_data.get("http") # 设置 ip:port

        return None

    def set(self, command):

        self.output_cmd(command)

        return os.system(command)

    def set_command_group(self, command_list, msg=""):
        """
        设置命令 - 多条
        :param command_list:
        :return: None
        """

        self.output_msg("开始发送命令",msg)
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


        self.nginx_path = self.script_path + "/app_sh/nginx" # nginx 绝对路径
        self.nginx_conf_path = self.nginx_path + "/nginx.conf" # nginx.conf 绝对路径
        self.nginx_access_log_path = self.project_path + "logs/nginx/access.log" # access.log 绝对路径
        self.nginx_error_log_path = self.project_path + "logs/nginx/error.log" # error.log 绝对路径
        self.nginx_uwsgi_pass_path = self.uwsgi_sock_path # uwsgi.sock 绝对路径

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
        out = os.popen("ps -ef | grep uwsgi | grep {}".format(self.server_name)).read()
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

    def set_uwsgi_conf_file(self):
        """配置uwsgi.ini文件
        """
        self.output_msg("配置文件","uwsgi.ini")

        self.set_uwsgi_ini(self.uwsgi_ini_path, "chdir", self.project_path) # 服务路径
        self.set_uwsgi_ini(self.uwsgi_ini_path, "module", self.server_name+".wsgi:application") # 服务名
        self.set_uwsgi_ini(self.uwsgi_ini_path, "socket", self.uwsgi_sock_path) # sock路径
        self.set_uwsgi_ini(self.uwsgi_ini_path, "pidfile", self.uwsgi_pid_path) # pid文件 路径
        self.set_uwsgi_ini(self.uwsgi_ini_path, "daemonize", self.uwsgi_log_path) # ip:port
        self.set_uwsgi_ini(self.uwsgi_ini_path, "http", self.uwsgi_http) # ip:port

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

    def read_file(self, feil_path):

        with open(feil_path,"r") as f:
            for line in f:
                print(line)

        return None

    def set_nginx_conf_file(self, feil_path):
        """

        :param feil_path:
        :return:
        """

        self.output_msg("配置文件","Nginx.conf")

        set_data_list = ["listen","server_name","access_log","error_log","uwsgi_pass"]
        temp_path = self.nginx_path + "/nginx.temp"
        # open两个文件, 一个读, 一个写, 最后把被读的文件删除, 将被写入的文件改名为被读的文件
        with open(feil_path,"r") as f, open(temp_path, "w", encoding="utf-8") as f_temp:
            for line in f:
                for foo in set_data_list:
                    if line.find(foo) != -1: # 待修改行
                        if foo == "listen":
                            line = "        listen {};\n".format(self.nginx_listen)
                        elif foo == "server_name":
                            line = "        server_name {}; \n".format(self.nginx_server_name)

                        elif foo == "access_log":
                            line = "        access_log {} main; \n".format(self.nginx_access_log_path)

                        elif foo == "error_log":
                            line = "        error_log {}; \n".format(self.nginx_error_log_path)

                        elif foo == "uwsgi_pass":
                            line = "            uwsgi_pass unix:{}; \n".format(self.uwsgi_sock_path)

                        else:
                            line = ""

                        break
                    else: # 不需要修改
                        pass

                f_temp.write(line)
            os.remove(feil_path) # 删掉原来的conf文件
            os.rename(temp_path, feil_path) # 将temp文件改名为conf

        return None

    def output_msg(self, title="", msg="OK", *args, **kwargs):
        """
        输出日志
        :param msg: 日志内容
        :return: None
        """

        print("--- {}: {} ".format(title, msg).ljust(60-self.string_chinese_count(title+msg),"-")) # 不够60个字符, 左边补"+"
        return None

    def output_cmd(self,  msg="", *args, **kwargs):
        """
        输出命令日志
        :param msg: 日志内容
        :return: None
        """

        print("*** 正在执行命令: {} ".format(msg).ljust(60-self.string_chinese_count(msg),"*")) # 不够60个字符, 左边补"+"
        return None

    def output_system(self, *args, **kwargs):
        """
        输出系统日志
        :param msg: 日志内容
        :return: None
        """

        print("++++++++++++++++++++ {} ".format(self.getName()).ljust(60-self.string_chinese_count(self.getName()), "+")) # 不够60个字符, 左边补"+"
        for title, msg in kwargs.items():
            print("++++++{}:{}".format(title, msg).ljust(60-self.string_chinese_count(title+msg), "+"))  # 不够60个字符, 左边补"+"
        print("++++++++++++++++++++ {} ".format(self.getName()).ljust(60-self.string_chinese_count(self.getName()), "+")) # 不够60个字符, 左边补"+"
        return None

    def string_chinese_count(self, msg=""):
        """
        统计字符串中, 中文的个数
        :param msg: 被统计的字符串
        :return: 中文的个数
        """

        count = len(re.findall(r'[\u4E00-\u9FFF]', msg))
        if isinstance(count,int):
            return count
        elif isinstance(count,float):
            return int(count)
        else:
            return 0

