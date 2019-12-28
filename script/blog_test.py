import sys
from base.base import MyBasePyScript


class MyTerminal(MyBasePyScript):

    def __init__(self, **payload):
        MyBasePyScript.__init__(self, **payload)

    def do_test00(self):

        print("===================== 进入 服务脚本 ==========================")

        if self.state == "start": # 开启服务

            print("===================== 启动服务 start ==========================")
            self.set_nginx_conf_file(self.nginx_conf_path) # 配置nginx.conf文件
            self.set_uwsgi_conf_file() # 配置uwsgi.ini文件
            uwsgi_cmd_list = ["uwsgi --ini {}/uwsgi.ini".format(self.uwsgi_path),]
            self.set_command_group(uwsgi_cmd_list, "uwsgi") # 启动uwsgi
            nginx_cmd_list = ["{}".format(self.nginx_start_cmd),]
            self.set_command_group(nginx_cmd_list, "nginx") # 启动nginx

        elif self.state == "stop": # 结束服务

            print("===================== 杀死服务 stop ==========================")

            uwsgi_pid_list = self.get_uwsgi_pid()  # 获取uwsgi的所有进程
            nginx_pid_list = self.get_nginx_pid()  # 获取nginx的所有进程
            self.kill_pid(uwsgi_pid_list)  # 杀死uwsgi的所有进程
            self.kill_pid(nginx_pid_list)  # 杀死uwsgi的所有进程

        elif self.state == "restart":  # 重启服务

            print("===================== 重启服务 restart ==========================")

            uwsgi_cmd_list = ["uwsgi --ini {}/uwsgi.ini".format(self.uwsgi_path),]
            self.set_command_group(uwsgi_cmd_list)
            nginx_cmd_list = ["{}".format(self.nginx_restart_cmd),]
            self.set_command_group(nginx_cmd_list)

        else:
            pass


        print("===================== 退出 服务脚本 ==========================")

        return None


    def do_test(self):
        print("oooo")
        return None

    def do_init(self):
        """
        基类自定义初始化
        :return:
        """
        print("$$$$$$$$$$$$$$$$$$$$$$$$$ 线程已开启 $$$$$$$$$$$$$$$$$$$$$$$$$")

        self.set_sys_data() # 根据系统的不一样, 设置不同的信息
        self.set_path() # 设置路径

        return None

    def do_exit(self):

        if self.state != "stop":
            print("==== 系统: {} ".format(self.sys_version))
            print("==== 服务名: {} ".format(self.server_name))
            print("==== 服务路径: {} ".format(self.project_path))
            print("==== 脚本路径: {} ".format(self.script_path))
            print("==== uwsgi路径: {} ".format(self.uwsgi_path))
            print("======== uwsgi_http: {} ".format(self.uwsgi_http))
            print("======== uwsgi.ini 路径: {} ".format(self.uwsgi_ini_path))
            print("======== uwsgi.sock 路径: {} ".format(self.uwsgi_sock_path))
            print("======== uwsgi.log 路径: {} ".format(self.uwsgi_log_path))
            print("======== uwsgi.pid 路径: {} ".format(self.uwsgi_pid_path))
            print("==== nginx路径: {} ".format(self.nginx_path))
            print("======== nginx.监听端口: {} ".format(self.nginx_listen))
            print("======== nginx.域名: {} ".format(self.nginx_server_name))
            print("======== nginx.access日志: {} ".format(self.nginx_access_log_path))
            print("======== nginx.error日志: {} ".format(self.nginx_error_log_path))

        print("$$$$$$$$$$$$$$$$$$$$$$$$$ 线程已结束 $$$$$$$$$$$$$$$$$$$$$$$$$")

        return None





