from datetime import date, datetime
import json


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

