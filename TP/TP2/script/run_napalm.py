'''Napalm'''

import os
import json
from napalm import get_network_driver


def get_inventory(inventory) -> dict:
    '''Get inventory from file'''
    with open(f"inventory/{inventory}", encoding="utf8") as json_file:
        data = json.load(json_file)

    return data


def deploy_config_ospf(inventory_dict) -> None:
    '''Deploy config ospf on routers from configs/OSPF_{hostname}.conf'''
    for device in inventory_dict:
        if "R" in device.get('device_name'):
            hostname = device.get('device_name')
            driver = get_network_driver('ios')
            device.pop('device_name')
            device_connect = driver(**device)
            device.update({"device_name": hostname})
            device_connect.open()
            device_connect.load_merge_candidate(filename=f'configs/OSPF_{hostname}.conf')
            print(f"Changes on device {hostname} :\n", device_connect.compare_config())

            try:
                choice = input("\nWould you like to commit these changes? [yN]: ")

            except NameError:
                choice = input("\nWould you like to commit these changes? [yN]: ")

            if choice == "y":
                print("Committing ...")
                device_connect.commit_config()
                print("Commit successful")
                rollback = input("\nWould you like to rollback? [yN]: ")
                if rollback == "y":
                    print("Rolling back ...")
                    device_connect.rollback()
                    print("Rollback successful")

            else:
                print("Discarding ...")
                device_connect.discard_config()

            device_connect.close()
            print("Done")


def deploy_config_merged(inventory_dict) -> None:
    '''Deploy config on all devices from configs/{hostname}.conf (using merge)'''
    for device in inventory_dict:
        hostname = device.get('device_name')
        driver = get_network_driver('ios')
        device.pop('device_name')
        device_connect = driver(**device)
        device.update({"device_name": hostname})
        device_connect.open()
        device_connect.load_merge_candidate(filename=f'configs/{hostname}.conf')
        print(f"Changes on device {hostname} :\n", device_connect.compare_config())

        try:
            choice = input("\nWould you like to commit these changes? [yN]: ")

            if choice.lower() == 'y':
                device_connect.commit_config()
                print(f"\nChanges committed on device {hostname}")

            else:
                device_connect.discard_config()
                print(f"\nChanges discarded on device {hostname}")

        except NameError as error:
            print(f"\nError: {error}")

        device_connect.close()


def deploy_config_replace(inventory_dict) -> None:
    '''Deploy config on all devices from configs/{hostname}.conf (using replace)'''
    for device in inventory_dict:
        hostname = device.get('device_name')
        driver = get_network_driver('ios')
        device.pop('device_name')
        device_connect = driver(**device)
        device.update({"device_name": hostname})
        device_connect.open()
        device_connect.load_replace_candidate(filename=f'configs/{hostname}.conf')
        print(f"Changes on device {hostname} :\n", device_connect.compare_config())

        try:
            choice = input("\nWould you like to commit these changes? [yN]: ")

            if choice.lower() == 'y':
                device_connect.commit_config()
                print(f"\nChanges committed on device {hostname}")

            else:
                device_connect.discard_config()
                print(f"\nChanges discarded on device {hostname}")

        except NameError as error:
            print(f"\nError: {error}")

        device_connect.close()


def backup_config(inventory_dict):
    '''Backup config for all devices in inventory'''
    for device in inventory_dict:
        hostname = device.get('device_name')
        driver = get_network_driver('ios')
        device.pop('device_name')
        device_connect = driver(**device)
        device.update({"device_name": hostname})
        device_connect.open()
        output = device_connect.get_config().get('running')
        device_connect.close()
        target_path = 'backup_cfg_napalm'

        # Create target directory if it does not exist
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        with open(f"backup_cfg_napalm/{hostname}.bak", "w", encoding="utf8") as file:
            file.write(output)


def deploy_bakcup_config(inventory_dict) -> None:
    '''Deploy backup config from backup_cfg_napalm/{hostname}.bak for all devices in inventory'''
    for device in inventory_dict:
        hostname = device.get('device_name')
        driver = get_network_driver('ios')
        device.pop('device_name')
        device_connect = driver(**device)
        device.update({"device_name": hostname})
        device_connect.open()
        device_connect.load_merge_candidate(filename=f'backup_cfg_napalm/{hostname}.bak')
        print(f"\nChanges on device {hostname} :\n", device_connect.compare_config())

        try:
            choice = input("\nWould you like to commit these changes? [yN]: ")

            if choice.lower() == 'y':
                device_connect.commit_config()
                print(f"\nChanges committed on device {hostname}")

            else:
                device_connect.discard_config()
                print(f"\nChanges discarded on device {hostname}")

        except NameError as error:
            print(f"\nError: {error}")

        device_connect.close()
