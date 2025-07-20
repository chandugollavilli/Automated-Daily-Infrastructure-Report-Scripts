import configparser
import json
import os
import random

def main():
    config = configparser.ConfigParser()
    config.read("/home/ubuntu/daily_infrastructure_report/config/config.ini")

    servers = config["SERVERS"]
    data_dir = config["PATHS"]["data_dir"]
    
    all_disk_usage = {}

    # Generate dummy data for disk usage
    for server_name, server_address in servers.items():
        hostname = server_address.split("@")[1]
        disk_data = [
            {
                "filesystem": "/dev/sda1",
                "size": f"{random.randint(100, 500)}G",
                "used": f"{random.randint(10, 90)}G",
                "avail": f"{random.randint(10, 410)}G",
                "use_percent": f"{random.randint(5, 95)}%",
                "mounted_on": "/"
            },
            {
                "filesystem": "/dev/sdb1",
                "size": f"{random.randint(500, 1000)}G",
                "used": f"{random.randint(50, 450)}G",
                "avail": f"{random.randint(50, 550)}G",
                "use_percent": f"{random.randint(10, 90)}%",
                "mounted_on": "/data"
            }
        ]
        all_disk_usage[hostname] = disk_data

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    output_file = os.path.join(data_dir, "disk_usage.json")
    with open(output_file, "w") as f:
        json.dump(all_disk_usage, f, indent=4)
    print(f"Dummy disk usage data saved to {output_file}")

if __name__ == "__main__":
    main()


