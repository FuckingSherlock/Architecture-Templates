from framework.urls import routes, fronts
from urllib.parse import parse_qs


class Main:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '/')
        if not path.endswith('/'):
            path += '/'

        method = environ['REQUEST_METHOD']
        post_data = get_data = None

        if method == 'GET':
            get_data = parse_qs(environ.get('QUERY_STRING', ''))
        elif method == 'POST':
            post_data = self.get_post_data(environ)

        if path in self.routes:
            view = self.routes[path]
        else:
            view = self.routes['NONE']
        request = {'method': method, 'get_data': get_data, 'post_data': post_data}

        for front in self.fronts:
            front(request)

        status, response_body = view(request)
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        return [response_body.encode('utf-8')]

    @staticmethod
    def get_post_data(environ):
        content_length = int(environ.get('CONTENT_LENGTH', '0'))
        if content_length > 0:
            post_data = environ['wsgi.input'].read(content_length)
        else:
            post_data = b''
        post_data = post_data.decode('utf-8')
        post_data = parse_qs(post_data)
        return post_data


application = Main(routes, fronts)
