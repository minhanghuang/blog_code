import sys
from sql_test import MySqlClass


def error_msg():
    print("请输入: web/sql/all and start/stop/restart or help, 例如: python3 blog.py web start")
    print("--- python3 blog.py web start : 只对uwsgi & Nginx操作 开启")
    print("--- python3 blog.py web stop : 只对uwsgi & Nginx操作 关闭")
    print("--- python3 blog.py web restart : 只对uwsgi & Nginx操作 重启")
    print("--- python3 blog.py sql start : 只对 数据库 操作 重置")
    print("--- python3 blog.py sql stop : 无效")
    print("--- python3 blog.py sql restart : 无效")
    print("--- python3 blog.py all start : uwsgi & Nginx & 数据库 重置")
    print("--- python3 blog.py all stop : 只对uwsgi & Nginx操作 关闭")
    print("--- python3 blog.py all restart : 只对uwsgi & Nginx操作 关重启闭")

    print("服务脚本没有启动")
    return None

if __name__ == "__main__":
    try:
        server = sys.argv[1] # 参数1
        state = sys.argv[2] # 参数2
    except:
        state = ""
        server = ""

    if  server not in ["web","sql","all"] or state not in ["start","stop","restart"] :
        error_msg()
    else:

        if "web" == server and "start" == state: # 只打开 web
            web_state = "start"
            sql_state = "stop"

        elif "web" == server and "stop" == state: # 停止 web
            web_state = "stop"
            sql_state = "stop"

        elif "web" == server and "restart" == state: # 重启 web
            web_state = "restart"
            sql_state = "stop"

        elif "sql" == server and "start" == state: # 重置 MySQL
            web_state = "stop"
            sql_state = "start"

        elif "all" == server and "start" == state: # 打开 web & MySQL
            web_state = "start"
            sql_state = "start"

        elif "all" == server and "stop" == state: # 停止 web
            web_state = "stop"
            sql_state = "stop"

        elif "all" == server and "restart" == state: # 重启 web
            web_state = "restart"
            sql_state = "stop"

        else:
            web_state = "pass"
            sql_state = "pass"
            error_msg()

        payload = {
            "web_state": web_state, # web 状态
            "sql_state": sql_state, # sql 状态
            "server_name": "blog_code",  # 服务名
            "python_evn": "python3",  # Python环境变量
        }
        mysqltest = MySqlClass(**payload)  # 数据库线程 实例化
        mysqltest.setName("数据库自动化-线程1")  # 设置线程名
        mysqltest.start()  # 开始

