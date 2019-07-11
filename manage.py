import settings
from application import Application
import tornado.ioloop

if __name__ == '__main__':
    app = Application()
    app.listen(settings.options['port'])
    tornado.ioloop.IOLoop.current().start()
