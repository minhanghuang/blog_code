

init_data = { # 所有初始化数据
    "redis":{
        "basedb":{ # 基本的数据库
            "host": "127.0.0.1",
            "port": 6379,
            "db": 0,
        },
        "celerydb":{ # celery中间人数据库
            "host": "127.0.0.1",
            "port": 6379,
            "db": 1,
        }
    },
    "ttf":{ # 字体
        "Linux":"/usr/share/fonts/windows/msyh.ttf", # 支持中文
        "Mac":"/System/Library/Fonts/Monaco.dfont", # 不支持中文
        "Windows":"C:/Windows/Fonts/STFANGSO.ttf",
    }
}