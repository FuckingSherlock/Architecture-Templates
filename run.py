import os
import sys
if 1:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'framework')))
from wsgiref.simple_server import make_server
from framework.main import application


with make_server('127.0.0.1', 8080, application) as httpd:
    sa = httpd.socket.getsockname()
    print(f'Serving HTTP on" http://{sa[0]}:{sa[1]}')
    httpd.serve_forever()
