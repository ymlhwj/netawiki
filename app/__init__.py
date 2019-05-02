import tornado.web
import pyrestful.rest
import tornado.httpserver

from app.views.content import NetaList, NetaContent, NetaComment, Test
from app.views.user import User


def create_server():
    app = pyrestful.rest.RestService([NetaList, NetaContent, NetaComment, User, Test], debug=True)
    return tornado.httpserver.HTTPServer(app)

