'''Main module => Entry point of the program'''

#-Imports-#
import yaml
from yaml.loader import SafeLoader
from create_save_config import render_network_config, save_built_config

#-Load DATA-#
with open('DATA/ESW2.yml', 'r', encoding='utf8') as file:
    ESW2_DATA = yaml.load(file, Loader=SafeLoader)

with open('DATA/R2.yml', 'r', encoding='utf8') as file:
    R2_DATA = yaml.load(file, Loader=SafeLoader)

with open('DATA/ESW4.yml', 'r', encoding='utf8') as file:
    ESW4_DATA = yaml.load(file, Loader=SafeLoader)


#-Create configs-#
def main():
    '''Main function'''

    esw2_conf = render_network_config('template_switches.j2', ESW2_DATA)
    save_built_config(esw2_conf, 'ESW2.conf')
    esw4_conf = render_network_config('template_switches.j2', ESW4_DATA)
    save_built_config(esw4_conf, 'ESW4.conf')
    r2_conf = render_network_config('template_routers.j2', R2_DATA)
    save_built_config(r2_conf, 'R2.conf')


if __name__ == '__main__':
    main()
