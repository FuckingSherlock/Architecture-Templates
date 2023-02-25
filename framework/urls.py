from datetime import date
from views import *


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/authors/': Authors(),
    '/contact/': Contact(),
    '/send_message/': SendMessage(),
    'NONE': PageNotFound404()
}
