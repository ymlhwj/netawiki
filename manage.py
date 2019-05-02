import tornado.ioloop
from app import create_server
import tornado.options

server = create_server()


if __name__ == "__main__":
    server.listen(8082)
    tornado.options.parse_command_line()
    print("netawiki server start")
    tornado.ioloop.IOLoop.current().start()
