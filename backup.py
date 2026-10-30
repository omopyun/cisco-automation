from getpass import getpass
from pathlib import Path

from netmiko import ConnectHandler

# 失敗
DEVICES = {
    "R1": "192.168.1.1",
    "R2": "192.168.1.2",
    "S1": "192.168.1.11",
    "S2": "192.168.1.21",
}

username = input("usernaame: ")
password = getpass("password: ")

backup_dir = Path("backup")
backup_dir.mkdir(exist_ok=True)

for name, ip in DEVICES.items():
    dev = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }
    try:
        with ConnectHandler(**dev) as conn:
            config = conn.send_command("show run | include hostname")
        (backup_dir / f"{name}.cfg").write_text(config, encoding="utf-8")
        print(f"{name}: OK")
    except Exception as e:
        print(f"{name}: 失敗 ({type(e).__name__})")