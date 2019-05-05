import tornado.web
import pyrestful.rest
import tornado.httpserver
import tornado.web

from app.views.content import NetaList, NetaContent, NetaComment, Test
from app.views.user import User, LoginHandler, LogoutHandler, UnLoginHandler


def create_server():
    app_settings = {"cookie_secret": "adfSa0ghG+sdgSD",
                    "login_url": "/user/unlogin"}
    app = pyrestful.rest.RestService([NetaList, NetaContent, NetaComment, User, Test,
                                      LoginHandler, LogoutHandler, UnLoginHandler], debug=True,
                                     **app_settings)
    return tornado.httpserver.HTTPServer(app)

