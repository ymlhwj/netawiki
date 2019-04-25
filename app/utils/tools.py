import json

class JsonUtils:
    """

    """
    @staticmethod
    def returm_json_response(code, msg, data):
        return json.dumps({"code": code, "msg": msg, "data": data})
