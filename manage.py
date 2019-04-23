import tornado.ioloop
from app import create_app

app = create_app()


if __name__ == "__main__":
    app.listen()
    tornado.ioloop.IOLoop.current().start()