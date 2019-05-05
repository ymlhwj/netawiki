# coding=utf-8
import pyrestful.rest
from pyrestful import mediatypes
from pyrestful.rest import get,post

from app.handlers.auth import AuthRestHandler
from app.utils.DBconnection import excute_query, excute_update, excute_delete
from app.utils.tools import Response, encrypt_md5


class User(pyrestful.rest.RestHandler):
    @post('/user/signup')
    def signUp(self):
        """
        用户注册
        :return:
        """
        pass

    @post('/user/changepassword')
    def changePassword(self):
        pass

class LoginHandler(pyrestful.rest.RestHandler):
    @post('/user/login', _produces=mediatypes.APPLICATION_JSON)
    def login(self, request):
        """
        用户登录
        :return:
        """
        params = {}
        params['username'] = request['username']
        params['password'] = encrypt_md5(request['password'])
        check_sql = """select username,password,role from netawiki.t_user where username = :username"""
        result = excute_query(check_sql, {'username': params['username']})
        if len(result) == 0:
            return Response.return_response(code=401.1, msg="user doesn'y exist")
        if result[0][1] != params['password']:
            return Response.return_response(code=401.1, msg="incorrect password")
        self.set_secure_cookie('username', params['username'])
        return Response.return_response(code=200, msg="login success")


class LogoutHandler(AuthRestHandler):
    @post('/user/logout', _produces=mediatypes.APPLICATION_JSON)
    def logout(self, request):
        if request["logout"]:
            self.clear_cookie("username")
        return Response.return_response(code=200, msg="logout success")


class UnLoginHandler(pyrestful.rest.RestHandler):
    @post('/user/unlogin', _produces=mediatypes.APPLICATION_JSON)
    def unLogin(self):
        return Response.return_response(code=403.1, msg="user doesn't login", data={'login': False})





