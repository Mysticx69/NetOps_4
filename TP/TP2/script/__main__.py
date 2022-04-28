# import
from re import template
from script.paramiko_ssh import write_remote_SSH, save_config
from script.create_config import (
    create_vlan_config_cpe_marseille,
    create_vlan_config_cpe_paris,
    render_network_config,
    save_built_config,
    create_R1_config,
)
from script.netmiko_ssh import get_inventory, get_config_int_admin_router, deploy_config


def build():

    # Create configs
    ESW2, R2 = create_vlan_config_cpe_marseille()
    ESW3, R3 = create_vlan_config_cpe_paris()
    R1 = create_R1_config()

    save_built_config(ESW2, "ESW2")
    save_built_config(R2, "R2")
    save_built_config(R3, "R3")
    save_built_config(ESW3, "ESW3")
    save_built_config(R1, "R1")


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
    inventory = "inventory/hosts.json"
    inventory_data = get_inventory(inventory)
    deploy_config(inventory_data)
