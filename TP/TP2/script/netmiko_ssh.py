"""Netmiko module"""
import json
import os
from netmiko import ConnectHandler


def get_inventory(json_file) -> str:
    '''Get inventory from file'''
    with open(f"{json_file}", encoding="utf8") as json_file:
        data = json.load(json_file)

    return data


def get_config_int_admin_router(inventory_data) -> None:
    '''Get config from router'''
    output = ""
    for device in inventory_data:
        hostname = device.get("hostname")
        if "R" in device.get("hostname"):
            device.pop("hostname")
            net_connect = ConnectHandler(**device)
            device.update({"hostname": hostname})
            output += f"\nConfig de l'interface admin de {hostname} : \n{net_connect.send_command('sh run int g0/0.99')}"
            net_connect.disconnect()


def deploy_config(inventory_data) -> None:
    '''Deploy config to devices'''
    for device in inventory_data:
        hostname = device.get("hostname")
        device.pop("hostname")
        net_connect = ConnectHandler(**device)
        device.update({"hostname": hostname})
        output = net_connect.send_config_from_file(f"configs/{hostname}.conf")
        net_connect.save_config()
        print(output)
        net_connect.disconnect()


def deploy_backup_config(inventory_data) -> None:
    '''Deploy backup config to devices'''
    for device in inventory_data:
        hostname = device.get("hostname")
        device.pop("hostname")
        net_connect = ConnectHandler(**device)
        device.update({"hostname": hostname})
        output = net_connect.send_config_from_file(f"backup_cfg/{hostname}.conf")
        net_connect.save_config()
        print(output)
        net_connect.disconnect()


def save_config(inventory_data) -> None:
    '''Save config to file'''
    for device in inventory_data:
        hostname = device.get("hostname")
        device.pop("hostname")
        net_connect = ConnectHandler(**device)
        device.update({"hostname": hostname})
        output = net_connect.send_command("sh run")
        target_path = 'backup_cfg'
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        with open(f"backup_cfg/{hostname}.conf", "w", encoding="utf8") as file:
            file.write(output)
