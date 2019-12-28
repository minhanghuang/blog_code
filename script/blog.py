import sys
from base.base import MyBasePyScripy



class MyTerminal(MyBasePyScripy):

    def __init__(self, **payload):
        MyBasePyScripy.__init__(self, **payload)

    def do_test(self):

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





if __name__ == "__main__":
    try:
        state = sys.argv[1]
    except:
        state = ""

    if state not in ["start","stop","restart"]:
        print("请输入: start / stop / restart, 例如: python3 blog.py start")
        print("服务脚本没有启动")
        has_gpus = False
    else:
        has_gpus = True

    if has_gpus:
        payload = {
            "state":state,
            "server_name":"blog_code",
        }
        terminal = MyTerminal(**payload)
        terminal.start()
        print("线程开启")

    else:
        pass
