from jinja2 import Environment, FileSystemLoader, Template
import os

env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


def render(template_name, **kwargs):
    template = env.get_template(template_name)
    return template.render(**kwargs)


def authors():
    tmpl = render('authors.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
    # template = env.get_template(tmpl)
    # return template.render()
    return tmpl


def about():
    return render('about.html')


def index():
    return render('index.html')


def add_handler():
    return [('/', index), ('/about/', about), ('/authors/', authors)]


print('hi')
