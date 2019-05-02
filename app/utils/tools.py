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


