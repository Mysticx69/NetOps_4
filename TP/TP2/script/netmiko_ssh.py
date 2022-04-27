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

# Show command that we execute.
command = "show ip int brief"

net_connect = ConnectHandler(**devices["R1"])
output = net_connect.send_command(
    command, use_textfsm=True
)  # use genie (pipenv install genie)

print(" Etat des interfaces sur R1 : \n")
for item in output:
    print(f'{item["intf"]} => {item["status"]}')


# # Show output
# print(f"\n{output}\n")
