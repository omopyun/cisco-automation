from getpass import getpass
from netmiko import ConnectHandler

SWITCHES = {"S1": "192.168.1.11", "S2": "192.168.1.21"}
COMMANDS = ["vlan 10", "name SALES", "vlan 20", "name DEV"]

username = input("username: ")
password = getpass("password: ")

for name, ip in SWITCHES.items():
    dev = {"device_type": "cisco_ios", "host": ip,
           "username": username, "password": password}
    try:
        with ConnectHandler(**dev) as conn:
            conn.send_config_set(COMMANDS)
        print(f"{name}: 投入OK")
    except Exception as e:
        print(f"{name}: 失敗 ({type(e).__name__})")
