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
# # Show command that we execute.
# command = "show ip int brief"

# net_connect = ConnectHandler(**devices["R1"])
# output = net_connect.send_command(
#     command, use_textfsm=True
# )  # use genie (pipenv install genie)

# print(" Etat des interfaces sur R1 : \n")
# for item in output:
#     print(f'{item["intf"]} => {item["status"]}')

# commands = [
#     "int lo0",
#     "ip add 192.168.1.1 255.255.255.255",
#     "descr loopback interface set by netmiko",
#     "exit",
# ]

# comand_del_lo = ["no int lo1", "no int lo2", "no int lo3", "no int lo4"]
# file = "configs/loopback_R01.conf"
# output = net_connect.send_config_from_file(file)
# print(output)

# net_connect.save_config()

# # Show output
# print(f"\n{output}\n")


def get_inventory(json_file):
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
            counter + +1

    return output


def deploy_config(inventory_data):

    for device in inventory_data:
        hostname = device.get("hostname")
        device.pop("hostname")
        net_connect = ConnectHandler(**device)
        file_config = f"configs/{hostname}.conf"
        output = net_connect.send_config_from_file(file_config)
        print(output)
