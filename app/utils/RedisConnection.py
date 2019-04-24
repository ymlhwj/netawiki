# coding=utf-8
# @Project : NetaWiki
# @Time    : 2019/4/24 0:27
# @Author  : baiasuka

import redis
import pickle

from ..settings import config


class RedisConnection:
    """
    直接将查询结果对象序列化存储
    """
    def __init__(self):
        # 创建对本机数据库的连接对象
        if config:
            self.host = config.REDIS_CACHE_CONFIG['host']
            self.port = config.REDIS_CACHE_CONFIG['port']
            self.db = config.REDIS_CACHE_CONFIG['db']
            self.expires = config.REDIS_CACHE_CONFIG['expired']
            self.password = config.REDIS_CACHE_CONFIG['password']
        self.conn = redis.Redis(host=self.host, port=self.port, db=self.db, password=self.password)

    # 存储
    def set(self, key_, value_, ex_=None):
        # 将数据pickle.dumps，转化为二进制bytes数据

        value_ = pickle.dumps(value_)
        # 将数据存储到数据库
        if ex_:
            self.conn.set(key_, value_, ex=ex_)
        else:
            self.conn.set(key_, value_, self.expires)
        return True

    # 读取
    def get(self, key_):
        # 从数据库根据键（key）获取值
        value_ = self.conn.get(key_)
        if value_:
            value_ = pickle.loads(value_)  # 加载bytes数据，还原为python对象
            return value_
        else:
            # 为None(值不存在)，返回空列表
            return None


if __name__ == "__main__":
    import pandas as pd
    rc = RedisConnection()
    data = pd.DataFrame({'A': [1, 2, 3]})
    rc.set('11100', data)
    print(rc.get("11100"))
