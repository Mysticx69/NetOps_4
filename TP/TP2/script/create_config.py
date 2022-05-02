"""Module to create different devices config using jinja2 templates and json data"""

## Imports
import json
from jinja2 import Environment, FileSystemLoader

## Load Json Data ##

SWITCH_DATA_ESW2 = "DATA/ESW2.json"
with open(SWITCH_DATA_ESW2, encoding="utf_8") as json_file:
    data_ESW2 = json.load(json_file)

ROUTER_DATA_R1 = "DATA/R1.json"
with open(ROUTER_DATA_R1, encoding="utf_8") as json_file:
    data_R1 = json.load(json_file)

ROUTER_DATA_R2 = "DATA/R2.json"
with open(ROUTER_DATA_R2, encoding="utf_8") as json_file:
    data_router = json.load(json_file)

ROUTER_DATA_R3 = "DATA/R3.json"
with open(ROUTER_DATA_R3, encoding="utf_8") as json_file:
    data_R3 = json.load(json_file)

SWITCH_DATA_ESW3 = "DATA/ESW3.json"
with open(SWITCH_DATA_ESW2, encoding="utf_8") as json_file:
    data_ESW3 = json.load(json_file)

env = Environment(loader=FileSystemLoader("templates"))

# Functions


def build() -> None:
    """Build all devices config"""
    # Create configs
    esw2, router2 = create_vlan_cpemarseille()
    esw3, router3 = create_vlan_cpeparis()
    router1 = create_config_r1()

    save_built_config(esw2, "ESW2")
    save_built_config(router2, "R2")
    save_built_config(router3, "R3")
    save_built_config(esw3, "ESW3")
    save_built_config(router1, "R1")


def render_network_config(file, data):
    """Return data processed from jinja2 template"""

    template = env.get_template(file)
    return template.render(data)


def create_config_r1():
    """Return R1 config"""
    router1 = render_network_config("template_router.j2", data_R1)

    return router1


def create_vlan_cpemarseille():
    """Create VLAN  config for CPE Marseille (router and switch)"""

    esw2 = render_network_config("template_switch.j2", data_ESW2)
    router2 = render_network_config("template_router.j2", data_router)
    return esw2, router2


def create_vlan_cpeparis():
    """Create VLAN  config for CPE Paris (router and switch)"""

    esw3 = render_network_config("template_switch.j2", data_ESW3)
    router3 = render_network_config("template_router.j2", data_R3)
    return esw3, router3


def save_built_config(config, filename):
    """Save built config to configs folder"""

    with open(f"configs/{filename}.conf", "w", encoding="utf_8") as fd1:
        fd1.write(config)
