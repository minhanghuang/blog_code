import requests


ip = "http://127.0.0.1:19800/"
password = input("请输入用户密码:")
ret = requests.post(
    url=ip,
    data={
        "password": password,
    }
)
print(ret)