import sys
from base.base import MyBasePyScripy



class MyTerminal(MyBasePyScripy):

    def __init__(self, **payload):
        MyBasePyScripy.__init__(self, **payload)

    def do_test(self):

        print("===================== 进入 服务脚本 ==========================")

        if self.state == "start": # 开启服务

            print("===================== 开启服务 start ==========================")

        elif self.state == "stop": # 结束服务

            print("===================== 结束服务 stop ==========================")

            uwsgi_pid_list = self.get_uwsgi_pid()  # 获取uwsgi的所有进程
            nginx_pid_list = self.get_nginx_pid()  # 获取nginx的所有进程
            self.kill_pid(uwsgi_pid_list)  # 杀死uwsgi的所有进程
            self.kill_pid(nginx_pid_list)  # 杀死uwsgi的所有进程

        else:
            pass


        print("===================== 退出 服务脚本 ==========================")

        return None











if __name__ == "__main__":
    try:
        state = sys.argv[1]
    except:
        state = ""

    if state not in ["start","stop"]:
        print("请输入: start Or stop, 例如: python3 blog.py start")
        print("服务脚本没有启动")
        has_gpus = False
    else:
        has_gpus = True

    if has_gpus:
        payload = {
            "state":state,
        }
        terminal = MyTerminal(**payload)
        terminal.start()
        print("线程开启")

    else:
        pass
