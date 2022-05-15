'''Create config from jinja2 templates and DATA file and save it.'''
import os
from pathlib import Path
from typing import Any
from jinja2 import Environment, FileSystemLoader
import yaml


def render_network_config(template_file, data_file, output_file) -> Any:
    '''Render config from jinja2 template and DATA file and save it.'''

    # Load template
    template_dir = Path(__file__).parent.parent / 'templates'
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)

    # Load data
    with open(f'DATA/{data_file}', 'r', encoding='utf8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # Render config
    config = template.render(data)

    # Save config

    # check if config folder exists
    if not os.path.exists('configs'):
        os.mkdir('configs')
    with open(f'configs/{output_file}', 'w', encoding='utf8') as file:
        file.write(config)

    return config


def create_config_cpe_bat_a() -> Any:
    '''Create config for CPE bat A.'''
    render_network_config('vlan_router.j2', 'R1_CPE_LYON_BAT_A.yml', 'R1_CPE_LYON_BAT_A.conf')
    render_network_config('vlan_router.j2', 'R2_CPE_LYON_BAT_A.yml', 'R2_CPE_LYON_BAT_A.conf')
    render_network_config('vlan_switch.j2', 'ESW1_CPE_LYON_BAT_A.yml', 'ESW1_CPE_LYON_BAT_A.conf')


def create_config_cpe_bat_b() -> Any:
    '''Create config for CPE bat B.'''
    render_network_config('vlan_router.j2', 'R1_CPE_LYON_BAT_B.yml', 'R1_CPE_LYON_BAT_B.conf')
    render_network_config('vlan_router.j2', 'R2_CPE_LYON_BAT_B.yml', 'R2_CPE_LYON_BAT_B.conf')
    render_network_config('vlan_switch.j2', 'ESW1_CPE_LYON_BAT_B.yml', 'ESW1_CPE_LYON_BAT_B.conf')
