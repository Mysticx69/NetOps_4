'''Nornir'''
#Imports#
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_configure, napalm_cli
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command, netmiko_save_config, netmiko_commit

nr = InitNornir(config_file="inventory/config.yaml")
print(nr.__dict__)
print(dir(nr.inventory.hosts.get("R1-CPE-BAT-A")))

for item in nr.inventory.hosts:
    print(nr.inventory.hosts.get(item).hostname)

print(nr.inventory.hosts.get("R1-CPE-BAT-A").keys())
print(nr.inventory.hosts.get("R1-CPE-BAT-A")["room"])
print(nr.inventory.hosts.get("R1-CPE-BAT-A").groups[0]["vendor"])
lst_host = [nr.inventory.hosts.get(item).hostname for item in nr.inventory.hosts]

print(nr.filter(device_type="router").inventory.hosts.keys())
print(nr.filter(device_type="router_switch").inventory.hosts.keys())


def hello_world(task: Task) -> Result:
    '''Test task'''
    return Result(host=task.host, result=f"{task.host.name} says hello world!")


result = nr.filter(device_type="router").run(task=hello_world)
print_result(result)
print_result(nr.run(task=napalm_cli, commands=["show ip interface brief"]))
