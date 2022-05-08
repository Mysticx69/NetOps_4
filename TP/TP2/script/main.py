"""Main file"""
# imports methods from local modules
from netmiko_ssh import get_inventory, deploy_config, save_config
from create_config import build


def main():
    """Main method to compute everything =>
    1. Build config from Jinja'as templates -> build()
    2. Get inventory and deploy config from files generated -> deploy_config()
    3. Save all configs in backup_cfg folder -> save_config()"""

    build()
    inventory_data = get_inventory("inventory/hosts.json")  # => Get inventory from file
    deploy_config(inventory_data)
    inventory_data_to_save = get_inventory("inventory/hosts.json")  # => Get inventory from file
    save_config(inventory_data_to_save)


if __name__ == "__main__":
    main()
