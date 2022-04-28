import paramiko
import time


def write_remote_SSH(dict_devices, commands):

    ssh = paramiko.SSHClient()  # initialization of SSHClient class

    # Set policy to use when connecting to servers without a known host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for device in dict_devices:
        ssh.connect(
            dict_devices[device].get("ip"),
            port=22,
            username=dict_devices[device].get("username"),
            password=dict_devices[device].get("password"),
            look_for_keys=False,
            allow_agent=False,
        )
        # The maximum amount of data to be received at once is specified by nbytes
        nbytes = 65535

        remote_conn = ssh.invoke_shell()  # invok shell

        for command in commands:
            remote_conn.send(f"{command}\n")  # Send $command
            time.sleep(2)
            output = remote_conn.recv(nbytes)  # Get output data from the channel
            print(output.decode("utf-8"))  # Decode

        ssh.close()  # Close SSH session


def save_config(dict_device_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for device in dict_device_name:
        ssh.connect(
            dict_device_name[device].get("ip"),
            port=22,
            username=dict_device_name[device].get("username"),
            password=dict_device_name[device].get("password"),
            look_for_keys=False,
            allow_agent=False,
        )
        # The maximum amount of data to be received at once is specified by nbytes
        nbytes = 65535

        remote_conn = ssh.invoke_shell()  # invok shell
        command = "sh run"

        remote_conn.send(f"{command}\n")  # Send $command
        time.sleep(20)
        output = remote_conn.recv(nbytes)  # Get output data from the channel
        f = open(f"configs/{device}_bck.conf", "a")
        f.write(output.decode("utf-8"))
        f.close()
