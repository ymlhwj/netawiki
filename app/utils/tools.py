import json

class JsonUtils:
    """
    前后端交互统一返回格式
        :param code: 返回码
        :param message: 返回信息
        :param data: 返回数据
        :return:
    """
    @staticmethod
    def returm_json_response(code, msg, data):
        return json.dumps({"code": code, "msg": msg, "data": data})


