from jinja2 import Template, Environment, FileSystemLoader
from yaml.loader import SafeLoader
import json
import yaml

switch_data = "DATA/ESW2.json"
with open(switch_data) as json_file:
   data_sw = json.load(json_file)

router_data = "DATA/R2.json"
with open(router_data) as json_file:
   data_router = json.load(json_file)

esw4_data = "DATA/ESW4.json"
with open(esw4_data) as json_file:
   data_ESW4 = json.load(json_file)

# Open the file and load the file
with open('DATA/ESW2.yaml') as f:
    data_sw_yaml = yaml.load(f, Loader=SafeLoader)
    print(data_sw_yaml)

env = Environment(loader=FileSystemLoader("templates"))

def render_network_config(file,data):

    template = env.get_template(file)
    return template.render(data)

def save_built_config(config,filename):
    #f = open("configs/{}.conf".format(filename), "w")
    f = open("configs/{}.conf".format(filename), "w")
    f.write(config)
    f.close()


ESW2 = render_network_config("template_switch.j2",data_sw_yaml)
R2 = render_network_config("template_router.j2",data_router)
ESW4 = render_network_config("template_switch.j2",data_ESW4)

save_built_config(ESW2,"ESW2")
save_built_config(R2,"R2")
save_built_config(ESW4,"ESW4")