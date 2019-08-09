# coding=utf-8
class Config:
    DB_HOST = '47.98.173.194'
    DB_USER = 'root'
    DB_PASSWORD = 'GTRawfQKiGmVIoFXSlcgdnlvZOXSO8'
    DB_NAME = 'netawiki'
    DB_PORT = 13306

    DIALECT = 'mysql'
    DRIVER = 'pymysql'

    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, DB_USER, DB_PASSWORD, DB_HOST,
                                                                              DB_PORT, DB_NAME)

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
