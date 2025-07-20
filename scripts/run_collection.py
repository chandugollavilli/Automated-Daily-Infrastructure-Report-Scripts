import subprocess
import os
import configparser

def run_script(script_path):
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        print(f"Successfully ran {script_path}")
        print(result.stdout)
        if result.stderr:
            print(f"Errors from {script_path}:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print(f"Error: python3 command not found. Make sure Python is installed and in your PATH.")

def main():
    config = configparser.ConfigParser()
    config.read("/home/ubuntu/daily_infrastructure_report/config/config.ini")
    data_dir = config["PATHS"]["data_dir"]

    # Ensure data directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("\n--- Collecting Running Servers ---")
    run_script(os.path.join(script_dir, "collect_running_servers.py"))

    print("\n--- Collecting Disk Usage ---")
    run_script(os.path.join(script_dir, "collect_disk_usage.py"))

    print("\n--- Collecting User Logins ---")
    run_script(os.path.join(script_dir, "collect_user_logins.py"))

    print("\n--- Collecting System Uptime ---")
    run_script(os.path.join(script_dir, "collect_system_uptime.py"))

    print("\n--- Data Collection Complete ---")

if __name__ == "__main__":
    main()


