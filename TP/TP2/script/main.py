"""Main Module"""
# imports methods from local modules
from create_config import build
from run_napalm import backup_config, get_inventory, deploy_config_replace, deploy_config_ospf, deploy_bakcup_config, deploy_config_merged


def main():
    """Main method to compute everything =>
    1. Build config from Jinja'as templates -> build()
    2. Get inventory and deploy config from files generated -> deploy_config()
    3. Save all configs in backup_cfg_napalm folder -> backup_config()"""

    build()
    inventory_napalm = get_inventory("inventory_napalm.json")
    deploy_config_replace(inventory_napalm)
    deploy_config_ospf(inventory_napalm)


if __name__ == "__main__":
    main()
