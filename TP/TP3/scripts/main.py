'''Main module'''

#Imports#
from create_config import create_config_cpe_bat_b, create_config_cpe_bat_a
from run_nornir import deploy_config_all


def main() -> None:
    '''Main function'''

    #Build conf
    create_config_cpe_bat_a()
    create_config_cpe_bat_b()

    #Deploy conf
    deploy_config_all()


if __name__ == '__main__':
    main()
