import pyrestful.rest


class AuthRestHandler(pyrestful.rest.RestHandler):
    """
    重载tornado.web.RequestHandler中的get_current_user方法
    接口继承该类可使用authenticated装饰器
    """
    def get_current_user(self):
        return self.get_secure_cookie("username")
