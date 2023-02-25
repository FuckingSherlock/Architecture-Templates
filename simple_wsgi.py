from templator import add_handler


class PageController:
    def __init__(self):
        self.handlers = {}

    def add_handler(self, url, handler):
        self.handlers[url] = handler

    def get_handler(self, url):
        return self.handlers.get(url)


class FrontController:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '/')
        if not path.endswith('/'):
            path += '/'
        handler = self.app.get_handler(path)
        if handler is not None:
            response_body = handler()
            status = '200 OK'
        else:
            response_body = 'Page Not Found'
            status = '404 Not Found'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        return [response_body.encode('utf-8')]


app = PageController()

for handler in add_handler():
    app.add_handler(handler[0], handler[1])


application = FrontController(app)
