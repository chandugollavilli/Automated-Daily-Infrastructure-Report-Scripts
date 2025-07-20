import configparser
import json
import os
import random

def main():
    config = configparser.ConfigParser()
    config.read("/home/ubuntu/daily_infrastructure_report/config/config.ini")

    servers = config["SERVERS"]
    data_dir = config["PATHS"]["data_dir"]
    
    running_servers_count = 0
    running_servers_list = []

    # Generate dummy data for running servers
    for server_name, server_address in servers.items():
        hostname = server_address.split("@")[1]
        if random.choice([True, False]): # Simulate some servers being down
            running_servers_count += 1
            running_servers_list.append(hostname)

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    output_file = os.path.join(data_dir, "running_servers.json")
    with open(output_file, "w") as f:
        json.dump({"count": running_servers_count, "servers": running_servers_list}, f, indent=4)
    print(f"Dummy running servers data saved to {output_file}")

if __name__ == "__main__":
    main()


