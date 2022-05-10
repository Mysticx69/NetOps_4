'''Napalm'''

import os
from napalm import get_network_driver


def deploy_config_ospf(inventory_dict):
    '''Deploy config'''
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


def backup_config(inventory_dict):
    '''Backup config'''
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
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        with open(f"backup_cfg_napalm/{hostname}.bak", "w", encoding="utf8") as file:
            file.write(output)
