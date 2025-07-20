# Daily Infrastructure Report Project: Automation and Scheduling

## 1. Introduction

This document describes how to automate the daily execution of the infrastructure report generation and distribution process. The primary method for scheduling this task in a Linux environment is using `cron`.

## 2. Setting up a Cron Job

`cron` is a time-based job scheduler in Unix-like computer operating systems. Users who set up and maintain software environments use `cron` to schedule jobs (commands or shell scripts) to run periodically at fixed times, dates, or intervals.

### 2.1. Prerequisites

Before setting up the cron job, ensure the following:

*   **Python Environment:** Python 3 and all required libraries (`paramiko`, `fpdf2`, `openpyxl`) are installed on the machine where the cron job will run.
*   **Script Permissions:** The `run_daily_report.py` script must have execute permissions. This was already set in the previous step using `chmod +x`.
*   **Configuration:** The `config.ini` file located at `/home/ubuntu/daily_infrastructure_report/config/config.ini` is correctly configured with server details, email settings, and file paths.

### 2.2. Cron Job Command

The main script that orchestrates the entire process is `run_daily_report.py`. This script is located at `/home/ubuntu/daily_infrastructure_report/scripts/run_daily_report.py`.

To schedule this script to run daily, for example, at 6:00 AM, you would add an entry to the crontab.

### 2.3. Editing the Crontab

To add or edit cron jobs, you use the `crontab` command. Each user has their own crontab file.

1.  **Open Crontab:**
    Open your user's crontab file for editing by running the following command in your terminal:
    ```bash
    crontab -e
    ```
    If this is your first time editing the crontab, you might be asked to choose a text editor.

2.  **Add the Cron Entry:**
    Add the following line to the end of the file. This line specifies that the script should run every day at 6:00 AM.
    ```cron
    0 6 * * * /usr/bin/python3 /home/ubuntu/daily_infrastructure_report/scripts/run_daily_report.py >> /home/ubuntu/daily_infrastructure_report/logs/cron.log 2>&1
    ```
    **Explanation of the cron entry:**
    *   `0`: Minute (0-59). Here, it's 0 minutes past the hour.
    *   `6`: Hour (0-23). Here, it's 6 AM.
    *   `*`: Day of the month (1-31). `*` means every day.
    *   `*`: Month (1-12). `*` means every month.
    *   `*`: Day of the week (0-7, where 0 or 7 is Sunday). `*` means every day of the week.
    *   `/usr/bin/python3`: The absolute path to the Python 3 interpreter. It's good practice to use the full path to avoid issues with the PATH environment variable in cron.
    *   `/home/ubuntu/daily_infrastructure_report/scripts/run_daily_report.py`: The absolute path to your script.
    *   `>> /home/ubuntu/daily_infrastructure_report/logs/cron.log 2>&1`: This redirects all standard output and standard error from the script to a log file. This is crucial for debugging and monitoring automated tasks.

3.  **Save and Exit:**
    Save the crontab file and exit the editor. If you are using `nano`, press `Ctrl+O`, then `Enter`, then `Ctrl+X`. If you are using `vi`/`vim`, press `Esc`, then type `:wq`, and press `Enter`.

    You should see a message like `crontab: installing new crontab`.

### 2.4. Verifying the Cron Job

To verify that your cron job has been added, you can view your crontab entries:

```bash
crontab -l
```

### 2.5. Ensuring Script Execution Permissions

While `chmod +x` makes the script executable, cron jobs often run with a minimal set of environment variables. It's important to ensure that the Python interpreter can find all necessary modules. Using absolute paths for the Python interpreter and the script helps. Additionally, ensure that the user under which the cron job runs has the necessary permissions to:

*   Read and write to the `data` and `reports` directories.
*   Read the `config.ini` file.
*   Execute the Python scripts.

## 3. Testing the End-to-End Automation

To test the full automation without waiting for the scheduled time, you can manually execute the `run_daily_report.py` script from the terminal:

```bash
python3 /home/ubuntu/daily_infrastructure_report/scripts/run_daily_report.py
```

This will trigger the data collection, report generation, and email simulation (or actual email sending if configured) process immediately. Check the `daily_infrastructure_report/reports` directory for generated files and the `daily_infrastructure_report/logs/cron.log` file for any output or errors.

## 4. Troubleshooting Common Cron Issues

*   **PATH Issues:** Cron jobs do not inherit the user's PATH environment variable. Always use absolute paths for commands and scripts.
*   **Environment Variables:** If your script relies on specific environment variables, define them within the cron job itself or at the top of your script.
*   **Permissions:** Ensure the script and its output directories have the correct read/write/execute permissions for the user running the cron job.
*   **Logging:** Always redirect output to a log file (`>> /path/to/log.log 2>&1`) to capture any errors or print statements, as cron jobs run silently in the background.
*   **Mail:** Cron can send an email with the output of the job if there is any. If you don't want this, redirect output to `/dev/null`.

## 5. Conclusion

By following these steps, the daily infrastructure report generation and distribution process will be fully automated, providing timely and consistent insights into your system's health. Regular monitoring of the cron log file is recommended to ensure the smooth operation of the automated task.


