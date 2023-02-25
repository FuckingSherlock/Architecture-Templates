from jinja2 import Environment, FileSystemLoader, exceptions
import os

env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))


def render(template_name, **kwargs):
    try:
        template = env.get_template(template_name)
    except exceptions.TemplateNotFound:
        return 'Template Not Found'
    return template.render(**kwargs)
