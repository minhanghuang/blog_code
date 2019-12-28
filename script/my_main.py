import sys
from blog_test import MyTerminal
from sql_test import MySqlClass


if __name__ == "__main__":
    try:
        state = sys.argv[1] # 参数
    except:
        state = ""

    if state not in ["start","stop","restart"]:
        print("请输入: start / stop / restart, 例如: python3 blog.py start")
        print("服务脚本没有启动")
    else:
        payload = {
            "state": state,
            "server_name": "blog_code", # 服务名
            "python_evn": "python3", # Python环境变量
        }
        # terminal = MyTerminal(**payload)
        # terminal.start()
        mysqltest = MySqlClass(**payload)
        mysqltest.start()