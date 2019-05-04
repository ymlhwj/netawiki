from datetime import date, datetime
import json
from hashlib import md5


class Response:
    """
    前后端交互统一返回格式
        :param code: 返回码
        :param message: 返回信息
        :param data: 返回数据
        :return:
    """
    @staticmethod
    def return_response(code, msg, data=None):
        if data is None:
            return {"code": code, "msg": msg}
        return {"code":code, "msg": msg, "data": data}

def format_data(columns, data):
    result = []
    for item in data:
        result.append(dict(zip(columns, item)))
    return result

class ComplexEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
      return obj.strftime('%Y-%m-%d')
    else:
      return json.JSONEncoder.default(self, obj)

# md5加密
def encrypt_md5(data, times=1):
    """
    :param data: 要加密的数据
    :param times: 解密的次数
    :return:
    """
    m5 = md5()
    for i in range(times):
        m5.update(data.encode("utf-8"))
        data = m5.hexdigest()
    return data

