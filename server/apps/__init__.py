# I Love China

__Author__ = 'Seenming'


from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def write_error(self, status_code: int, **kwargs) -> None:
        self.set_status(status_code, reason=kwargs.get("reason", ""))

