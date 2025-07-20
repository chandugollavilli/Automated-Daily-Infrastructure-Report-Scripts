import subprocess
import os

def run_script(script_path):
    try:
        result = subprocess.run(["python3", script_path], capture_output=True, text=True, check=True)
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
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("\n--- Starting Daily Infrastructure Report Generation ---")

    print("\n--- Step 1: Collecting Data ---")
    run_script(os.path.join(script_dir, "run_collection.py"))

    print("\n--- Step 2: Generating PDF Report ---")
    run_script(os.path.join(script_dir, "generate_pdf_report.py"))

    print("\n--- Step 3: Generating Excel Report ---")
    run_script(os.path.join(script_dir, "generate_excel_report.py"))

    print("\n--- Step 4: Sending Email Notification ---")
    run_script(os.path.join(script_dir, "send_email.py"))

    print("\n--- Daily Infrastructure Report Generation Complete ---")

if __name__ == "__main__":
    main()


