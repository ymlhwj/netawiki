import tornado.web
import pyrestful.rest

def create_app():
    return pyrestful.rest.RestService()

