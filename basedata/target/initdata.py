from datetime import timedelta
from celery.schedules import crontab


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
    },
    "celery":{
        "CELERY_BROKER_URL":"redis://127.0.0.1:6379/1", # 中间件
        "CELERY_ACCEPT_CONTENT":['json'],
        "CELERY_TASK_SERIALIZER":"json",
        "CELERY_RESULT_BACKEND":"redis://127.0.0.1:6379/2", # 数据结果存储地址
        "CELERY_TIMEZONE": 'Asia/Shanghai',
        "CELERY_BEAT_SCHEDULE":{
            'celery4_text': { # 任务名(随意起)
                'task': 'app_test.tasks.text', # 定时任务函数路径
                'schedule': timedelta(seconds=30), # 任务循环时间
                "args": (4,9), # 参数
            },
            'celery4_text2': { # 任务名(随意起)
                'task': 'app_test.tasks.text2', # 定时任务函数路径
                'schedule': timedelta(seconds=5), # 任务循环时间
                "args": (4,91), # 参数
            }
        }
    }
}
