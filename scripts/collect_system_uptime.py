import configparser
import json
import os
import random

def main():
    config = configparser.ConfigParser()
    config.read("/home/ubuntu/daily_infrastructure_report/config/config.ini")

    servers = config["SERVERS"]
    data_dir = config["PATHS"]["data_dir"]
    
    all_uptime_data = {}

    # Generate dummy data for system uptime
    for server_name, server_address in servers.items():
        hostname = server_address.split("@")[1]
        days = random.randint(0, 365)
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        uptime_str = f"up {days} days, {hours} hours, {minutes} minutes"
        all_uptime_data[hostname] = uptime_str

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    output_file = os.path.join(data_dir, "system_uptime.json")
    with open(output_file, "w") as f:
        json.dump(all_uptime_data, f, indent=4)
    print(f"Dummy system uptime data saved to {output_file}")

if __name__ == "__main__":
    main()

