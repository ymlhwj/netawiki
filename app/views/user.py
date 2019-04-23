import pyrestful.rest

from pyrestful.rest import get,post

class User(pyrestful.rest.RestHandler):
    @post('/user/signup')
    def signUp(self):
        """
        用户注册
        :return:
        """
        pass


