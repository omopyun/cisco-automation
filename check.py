from getpass import getpass
from netmiko import ConnectHandler

SWITCHES = {"S1": "192.168.1.11", "S2": "192.168.1.21"}  
EXPECTED = ["SALES", "DEV"]

username = input("username: ")
password = getpass("password: ")

for name, ip in SWITCHES.items():
    dev = {"device_type": "cisco_ios", "host": ip,
           "username": username, "password": password}
    try:
        with ConnectHandler(**dev) as conn:
            out = conn.send_command("show vlan brief")
        missing = [v for v in EXPECTED if v not in out]
        if missing:
            print(f"{name}: NG (見つからない: {', '.join(missing)})")
        else:
            print(f"{name}: OK")
    except Exception as e:
        print(f"{name}: 失敗 ({type(e).__name__})")