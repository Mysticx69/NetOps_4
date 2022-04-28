from jinja2 import Template, Environment, FileSystemLoader
import json

# Define Data
switch_data = "DATA/ESW2.json"
with open(switch_data) as json_file:
    data_ESW2 = json.load(json_file)

router_data = "DATA/R2.json"
with open(router_data) as json_file:
    data_router = json.load(json_file)

router_data = "DATA/R3.json"
with open(router_data) as json_file:
    data_R3 = json.load(json_file)

router_data = "DATA/R1.json"
with open(router_data) as json_file:
    data_R1 = json.load(json_file)

esw3_data = "DATA/ESW3.json"
with open(esw3_data) as json_file:
    data_ESW3 = json.load(json_file)


env = Environment(loader=FileSystemLoader("templates"))


# Functions
def render_network_config(file, data):

    template = env.get_template(file)
    return template.render(data)


def create_R1_config():
    R1 = render_network_config("template_router.j2", data_R1)

    return R1


def create_vlan_config_cpe_marseille():

    ESW2 = render_network_config("template_switch.j2", data_ESW2)
    R2 = render_network_config("template_router.j2", data_router)
    return ESW2, R2


def create_vlan_config_cpe_paris():

    ESW3 = render_network_config("template_switch.j2", data_ESW3)
    R3 = render_network_config("template_router.j2", data_R3)
    return ESW3, R3


def save_built_config(config, filename):

    f = open("configs/{}.conf".format(filename), "w")
    f.write(config)
    f.close()
