from templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


class About:
    def __call__(self, request):
        return '200 OK', render('about.html')


class Authors:
    def __call__(self, request):
        return '200 OK', render('authors.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])


class Contact:
    def __call__(self, request):
        return '200 OK', render('contacts.html')


class SendMessage:
    def __call__(self, request):
        print(__name__, request['post_data'])
        if request['method'] == 'POST':
            data = request['post_data']
            return '200 OK', render('message_sent.html', subject=data['subject'], message=data['message'], email=data['email'])

        return '200 OK', render('contacts.html')


class Search:
    def __call__(self, request):
        query = request['get_data'].get('query')
        if query:
            # Обработка GET запроса
            return '200 OK', f'<h1>Search results for "{query}"</h1>'.encode('utf-8')
        else:
            return '200 OK', b'<h1>Search form</h1><form><input name="query"><input type="submit"></form>'


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
