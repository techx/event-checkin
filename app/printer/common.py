from string import Template
from os.path import join, dirname


def fill_template(user):
    with open(join(dirname(__file__), 'labels', 'xfair.template'), 'r') as template_file:
        template = Template(template_file.read())
        return template.substitute(name=user.name, major=user.major, graduation=user.graduation)
