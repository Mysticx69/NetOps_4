"""Main Module"""
# imports methods from local modules
from time import sleep
from netmiko_ssh import get_inventory, deploy_config, save_config
from run_napalm import deploy_config_ospf, backup_config, deploy_bakcup_config
from create_config import build


def main():
    """Main method to compute everything =>
    1. Build config from Jinja'as templates -> build()
    2. Get inventory and deploy config from files generated -> deploy_config()
    3. Save all configs in backup_cfg folder -> save_config()"""

    # build()
    # inventory_data = get_inventory("inventory/hosts.json")  # => Get inventory from file
    # deploy_config(inventory_data)
    # sleep(10)
    # inventory_data_to_save = get_inventory("inventory/hosts.json")  # => Get inventory from file
    # save_config(inventory_data_to_save)
    # inventory_napalm = get_inventory("inventory/hosts_napalm.json")  # => Get inventory from file
    # deploy_config_ospf(inventory_napalm)
    inventory_data_napalm = get_inventory(
        "inventory/hosts_napalm.json")  # => Get inventory from file
    backup_config(inventory_data_napalm)
    deploy_bakcup_config(inventory_data_napalm)


if __name__ == "__main__":
    main()
