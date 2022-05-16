'''Main module'''

#Imports#
from create_config import create_config_cpe_bat_b, create_config_cpe_bat_a
from run_nornir import deploy_config_all, deploy_config_single


def main() -> None:
    '''Main function'''

    #Build conf
    create_config_cpe_bat_a()
    create_config_cpe_bat_b()

    #Deploy conf
    deploy_config_single("R1-CPE-BAT-A", "R1-CPE-BAT-A")


if __name__ == '__main__':
    main()
