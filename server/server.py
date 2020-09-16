# I Love China

__Author__ = 'Seenming'


import tornado.web
import tornado.ioloop


class App(tornado.web.Application):
    def __init__(self, **settings):
        handlers = []
        super().__init__(handlers, **settings)


if __name__ == '__main__':
    settings = {}
    app = App(**settings)
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
