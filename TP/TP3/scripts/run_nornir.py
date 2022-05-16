'''Nornir'''
#Imports#

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_configure, napalm_cli
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command, netmiko_save_config, netmiko_commit

nr = InitNornir(config_file="inventory/config.yaml")
# print(nr.__dict__)
# print(dir(nr.inventory.hosts.get("R1-CPE-BAT-A")))

# for item in nr.inventory.hosts:
#     print(nr.inventory.hosts.get(item).hostname)

# print(nr.inventory.hosts.get("R1-CPE-BAT-A").keys())
# print(nr.inventory.hosts.get("R1-CPE-BAT-A")["room"])
# print(nr.inventory.hosts.get("R1-CPE-BAT-A").groups[0]["vendor"])
# lst_host = [nr.inventory.hosts.get(item).hostname for item in nr.inventory.hosts]

# print(nr.filter(device_type="router").inventory.hosts.keys())
# print(nr.filter(device_type="router_switch").inventory.hosts.keys())

# def hello_world(task: Task) -> Result:
#     '''Test task'''
#     return Result(host=task.host, result=f"{task.host.name} says hello world!")

# result = nr.filter(device_type="router").run(task=hello_world)

# #32)
# int_routers = nr.filter(device_type="router").run(task=napalm_cli,
#                                                   commands=["show ip interface brief"])
# #33)
# arp_table = nr.filter(device_type="router_switch").run(task=napalm_get, getters=["arp_table"])

# #34)
# lo1_R1 = nr.filter(device_name="R1-CPE-BAT-A").run(
#     task=napalm_configure, configuration="interface lo1 \n ip add 1.1.1.1 255.255.255.255")
# lo1_R2 = nr.filter(device_name="R2-CPE-BAT-A").run(
#     task=napalm_configure, configuration="interface lo1 \n ip add 2.2.2.2 255.255.255.255")

# #35)
# save_conf = nr.run(task=napalm_cli, commands=["wr"])

# #36)
# int_netmiko = nr.filter(device_type="router").run(task=netmiko_send_command,
#                                                   command_string="show ip int br")
# #37)
# lo1_netmiko_r1 = nr.filter(device_name="R1-CPE-BAT-A").run(
#     task=netmiko_send_config, config_commands=["int lo2", "ip add 1.1.1.2 255.255.255.255"])
# lo1_netmiko_r2 = nr.filter(device_name="R2-CPE-BAT-A").run(
#     task=netmiko_send_config, config_commands=["int lo2", "ip add 2.2.2.3 255.255.255.255"])
# #38)
# int_netmiko_save = nr.run(task=netmiko_save_config)

# #39)


def deploy_config_all() -> None:
    """Load configuration into all hosts using nornir_napalm"""
    for host in nr.inventory.hosts:
        print_result(
            nr.filter(device_name=host).run(task=napalm_configure, filename=f'configs/{host}.conf'))
        # useless print_result(nr.filter(device_name=host).run(task=netmiko_save_config))


def deploy_config_single(host, config_file) -> None:
    """Load configuration into singe device using nornir_napalm"""
    print_result(nr.filter(device_name=host).run(task=napalm_configure, filename=config_file))
