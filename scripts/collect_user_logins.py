import configparser
import json
import os
import random
from datetime import datetime, timedelta

def main():
    config = configparser.ConfigParser()
    config.read("/home/ubuntu/daily_infrastructure_report/config/config.ini")

    servers = config["SERVERS"]
    data_dir = config["PATHS"]["data_dir"]
    
    all_user_logins = {}

    # Generate dummy data for user logins
    for server_name, server_address in servers.items():
        hostname = server_address.split("@")[1]
        login_data = []
        for _ in range(random.randint(5, 20)): # Simulate 5-20 login attempts
            timestamp = (datetime.now() - timedelta(minutes=random.randint(1, 1440))).isoformat()
            username = random.choice(["admin", "user1", "guest"])
            source_ip = f"192.168.1.{random.randint(1, 254)}"
            status = random.choice(["Success", "Failed"])
            login_data.append({
                "timestamp": timestamp,
                "hostname": hostname,
                "username": username,
                "source_ip": source_ip,
                "status": status
            })
        all_user_logins[hostname] = login_data

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    output_file = os.path.join(data_dir, "user_logins.json")
    with open(output_file, "w") as f:
        json.dump(all_user_logins, f, indent=4)
    print(f"Dummy user login data saved to {output_file}")

if __name__ == "__main__":
    main()


