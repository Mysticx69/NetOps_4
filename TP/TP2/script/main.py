"""Main file"""
# imports methods from local modules
from netmiko_ssh import get_inventory, deploy_config
from create_config import build


def main():
    """Main method to compute everything =>
    1. Build config from Jinja'as templates -> build()
    2. Get inventory and deploy config from files generated -> deploy_config()"""

    build()
    inventory_data = get_inventory("inventory/hosts.json")  # => Get inventory from file
    deploy_config(inventory_data)


if __name__ == "__main__":
    main()
