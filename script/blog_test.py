import sys
from base.base import MyBasePyScript


class MyTerminal(MyBasePyScript):

    def __init__(self, **payload):
        MyBasePyScript.__init__(self, **payload)

    def do_test(self):

        if self.web_state == "start": # 开启服务

            self.output_msg("启动服务", "start")
            self.set_nginx_conf_file(self.nginx_conf_path) # 配置nginx.conf文件
            self.set_uwsgi_conf_file() # 配置uwsgi.ini文件
            uwsgi_cmd_list = ["uwsgi --ini {}/uwsgi.ini".format(self.uwsgi_path),]
            self.set_command_group(uwsgi_cmd_list, "uwsgi") # 启动uwsgi
            nginx_cmd_list = ["{}".format(self.nginx_start_cmd),]
            self.set_command_group(nginx_cmd_list, "nginx") # 启动nginx

        elif self.web_state == "stop": # 结束服务

            self.output_msg("杀死服务","stop")
            uwsgi_pid_list = self.get_uwsgi_pid()  # 获取uwsgi的所有进程
            nginx_pid_list = self.get_nginx_pid()  # 获取nginx的所有进程
            self.kill_pid(uwsgi_pid_list)  # 杀死uwsgi的所有进程
            self.kill_pid(nginx_pid_list)  # 杀死uwsgi的所有进程

        elif self.web_state == "restart":  # 重启服务

            self.output_msg("重启服务","restart")
            uwsgi_cmd_list = ["uwsgi --ini {}/uwsgi.ini".format(self.uwsgi_path),]
            self.set_command_group(uwsgi_cmd_list)
            nginx_cmd_list = ["{}".format(self.nginx_restart_cmd),]
            self.set_command_group(nginx_cmd_list)

        else:
            pass

        return None

    def do_exit(self):

        if self.web_state != "pass": #

            sys_data = {
                "系统": self.sys_version,
                "服务名": self.server_name,
                "服务路径": self.project_path,
                "脚本路径": self.script_path,
                "uwsgi路径": self.uwsgi_path,
                "uwsgi_http": self.uwsgi_http,
                "uwsgi.ini 路径": self.uwsgi_ini_path,
                "uwsgi.sock 路径": self.uwsgi_sock_path,
                "uwsgi.log 路径": self.uwsgi_log_path,
                "uwsgi.pid 路径": self.uwsgi_pid_path,
                "nginx路径": self.nginx_path,
                "nginx.监听端口": self.nginx_listen,
                "nginx.域名": self.nginx_server_name,
                "nginx.access日志": self.nginx_access_log_path,
                "nginx.error日志": self.nginx_error_log_path,
            }
            self.output_system(**sys_data)

        return None





