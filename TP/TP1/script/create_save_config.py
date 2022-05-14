'''Create config from jinja2 templates and save it to configs folder'''

#-Imports-#
import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


def render_network_config(template, data) -> str:
    '''Create config from jinja template'''
    template = env.get_template(template)
    return template.render(data)


def save_built_config(config, filename) -> None:
    '''Save config to file'''
    # check if path exist
    if not os.path.exists('configs'):
        os.mkdir('configs')
    with open(f'configs/{filename}', 'w', encoding='utf8') as file:
        file.write(config)
