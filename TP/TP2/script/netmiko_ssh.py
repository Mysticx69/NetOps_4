"""Netmiko module"""
import json
from netmiko import ConnectHandler

devices = {
    "R1": {
        "device_type": "cisco_ios",
        "ip": "172.16.100.126",
        "username": "cisco",
        "password": "cisco",
    },
    "R2": {
        "device_type": "cisco_ios",
        "ip": "172.16.100.190",
        "username": "cisco",
        "password": "cisco",
    },
    "R3": {
        "device_type": "cisco_ios",
        "ip": "172.16.100.254",
        "username": "cisco",
        "password": "cisco",
    },
}


def get_inventory(json_file) -> str:
    with open(f"{json_file}") as json_file:
        data = json.load(json_file)

    return data


def get_config_int_admin_router(inventory_data):
    output = ""
    hostname = []
    for item in inventory_data:
        hostname.append(item["hostname"])

    counter = 0
    for device in inventory_data:
        if "R" in device.get("hostname"):
            device.pop("hostname")
            net_connect = ConnectHandler(**device)
            output += f"\nConfig de l'interface admin de {hostname[counter]} : \n{net_connect.send_command('sh run int g0/0.99')}"
            counter += 1

    return output


def deploy_config(inventory_data):

    for device in inventory_data:
        hostname = device.get("hostname")
        device.pop("hostname")
        net_connect = ConnectHandler(**device)
        file_config = f"configs/{hostname}.conf"
        output = net_connect.send_config_from_file(file_config)
        print(output)
