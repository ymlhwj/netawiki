# coding=utf-8
class Config:
    DB_HOST = '127.0.0.1'
    DB_USER = ''
    DB_PASSWORD = ''
    DB_NAME = ''
    DB_PORT = 2345

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_CACHE_DB = 1
    REDIS_PASSWORD = None
    REDIS_CACHE_DB_EXPIRED = 3600
    REDIS_CACHE_CONFIG = {
        "host": REDIS_HOST,
        "port": REDIS_PORT,
        "db": REDIS_CACHE_DB,
        "password": REDIS_PASSWORD,
        "expired": REDIS_CACHE_DB_EXPIRED  # ms
    }
    # 用于Celery的Redis配置项
    REDIS_CELERY_BROKER_DB = 5
    REDIS_CELERY_BACKEND_DB = 3




config = Config()