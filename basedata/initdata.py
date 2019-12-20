

init_data = {
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
    }
}