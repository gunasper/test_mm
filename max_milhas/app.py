import sys
import tornado.ioloop
import tornado.web

from routes import ROUTES
from tornado.log import enable_pretty_logging
from commons.sql_class import SQLMaxMilhas
import MySQLdb
import time
from datetime import datetime
PORT = 5000

class Application(tornado.web.Application):

    def __init__(self, ROUTES):
        settings = dict(
            debug=True
        )
        super(Application, self).__init__(ROUTES, **settings)
        self.up_time = int(time.time())
        self.up_time_iso = datetime.now().isoformat(' ')
        self.request_counter = 0

        SQLMaxMilhas(MySQLdb.connect(host="localhost", user="testuser",
                                     passwd="123456", db="maxmilhas"))


if __name__ == "__main__":
    enable_pretty_logging()
    args = sys.argv
    args.append("--log_file_prefix=my_app.log")
    tornado.options.parse_command_line(args)

    app = Application(ROUTES)
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
