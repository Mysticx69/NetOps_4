"""Main file"""

# imports
from create_config import (
    create_config_r1,
    create_vlan_cpeparis,
    create_vlan_cpemarseille,
    save_built_config,
)
from netmiko_ssh import get_inventory, deploy_config


def build():
    """Build all devices config user methods from create_config module"""
    # Create configs
    esw2, router2 = create_vlan_cpemarseille()
    esw3, router3 = create_vlan_cpeparis()
    router1 = create_config_r1()

    save_built_config(esw2, "ESW2")
    save_built_config(router2, "R2")
    save_built_config(router3, "r3")
    save_built_config(esw3, "esw3")
    save_built_config(router1, "R1")


if __name__ == "__main__":

    # dict of devices

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
    # liste des commandes pour paramiko
    commands_lo = [
        "conf t ",
        "int lo0",
        "ip add 192.168.1.1 255.255.255.255",
        "descr loopback interface set by paramiko 2",
        "exit",
    ]

    commands_sh_conf = ["sh run int lo0"]

    commands_add_desc = [
        "conf t",
        "int g0/0.99",
        "descr loopback interface set by paramiko 3",
        "exit",
    ]
    build()
    INVENTORY = "inventory/hosts.json"
    inventory_data = get_inventory(INVENTORY)
    deploy_config(inventory_data)
