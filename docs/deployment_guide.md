# Daily Infrastructure Report Project: Deployment Guide

## 1. Introduction

This Deployment Guide provides detailed instructions for deploying the Daily Infrastructure Report project in a production-like environment. It covers the necessary steps from preparing the server to configuring the application and setting up automated execution. This guide assumes a Linux-based server environment.

### 1.1. Purpose and Audience

This document is intended for system administrators, DevOps engineers, and IT professionals responsible for deploying and maintaining the Daily Infrastructure Report system. It aims to provide clear, actionable steps to ensure a successful and secure deployment.

### 1.2. Key Deployment Steps

The deployment process can be broken down into the following main phases:

1.  **Server Preparation:** Ensuring the target server meets all prerequisites.
2.  **Project Installation:** Transferring project files and installing dependencies.
3.  **Configuration:** Customizing the `config.ini` file for your environment.
4.  **SSH Key Setup:** Configuring secure, passwordless SSH access to target servers.
5.  **Automation Setup:** Scheduling the daily report generation using cron.
6.  **Verification:** Testing the end-to-end workflow.

## 2. Server Preparation

Before deploying the project, ensure your designated reporting server meets the following requirements:

### 2.1. Operating System

A fresh installation of a modern Linux distribution is recommended (e.g., Ubuntu Server 20.04+, CentOS 7+, Debian 10+).

### 2.2. Essential Packages

Install necessary system packages. For Debian/Ubuntu-based systems:

```bash
sudo apt update
sudo apt install python3 python3-pip git openssh-client
```

For CentOS/RHEL-based systems:

```bash
sudo yum update
sudo yum install python3 python3-pip git openssh-client
# Or for newer CentOS/RHEL:
sudo dnf update
sudo dnf install python3 python3-pip git openssh-client
```

### 2.3. User Account

It is recommended to create a dedicated, non-root user account for running the daily report script. This adheres to the principle of least privilege.

```bash
sudo adduser dailyreportuser
sudo usermod -aG sudo dailyreportuser # Grant sudo if needed for some operations, but try to avoid for cron
```

Switch to this user for the remaining steps:

```bash
su - dailyreportuser
```

### 2.4. Firewall Configuration

Ensure your firewall (e.g., `ufw` on Ubuntu, `firewalld` on CentOS) allows outbound connections on:

*   **SSH (Port 22):** To connect to target servers for data collection.
*   **SMTP (Ports 25, 465, or 587):** To connect to your SMTP server for email delivery.

**Example (UFW):**

```bash
sudo ufw allow out 22/tcp
sudo ufw allow out 587/tcp  # Or 465/tcp, 25/tcp depending on your SMTP server
```

## 3. Project Installation

### 3.1. Clone the Repository

Navigate to the home directory of your `dailyreportuser` and clone the project repository:

```bash
cd /home/dailyreportuser/
git clone <repository_url> daily_infrastructure_report
```

Replace `<repository_url>` with the actual URL of your Git repository. This will create the `daily_infrastructure_report` directory.

### 3.2. Create and Activate Python Virtual Environment

It is best practice to install Python dependencies within a virtual environment to isolate them from system-wide packages.

```bash
cd /home/dailyreportuser/daily_infrastructure_report
python3 -m venv venv
source venv/bin/activate
```

### 3.3. Install Python Dependencies

With the virtual environment activated, install the required Python libraries:

```bash
pip install paramiko fpdf2 openpyxl
```

### 3.4. Verify Script Permissions

Ensure the main execution script is executable:

```bash
chmod +x scripts/run_daily_report.py
```

## 4. Configuration

Edit the `config.ini` file located at `/home/dailyreportuser/daily_infrastructure_report/config/config.ini`.

```bash
nano config/config.ini
```

Update the following sections:

### 4.1. `[SERVERS]`

List all target servers from which data will be collected. Use `user@hostname_or_ip` format. Ensure the `user` has necessary permissions on the target server.

```ini
[SERVERS]
server1 = your_ssh_user@192.168.1.10
server2 = your_ssh_user@your-server-hostname.com
```

### 4.2. `[EMAIL]`

Configure your SMTP server details for sending reports. **For production, avoid storing passwords directly. Consider environment variables or a secrets manager.**

```ini
[EMAIL]
smtp_server = smtp.your-email.com
smtp_port = 587
smtp_username = your_email@example.com
smtp_password = your_email_password
recipient_emails = admin1@example.com, admin2@example.com
```

### 4.3. `[PATHS]`

Define the directories for data and reports. Ensure the `dailyreportuser` has write permissions to these directories.

```ini
[PATHS]
data_dir = /home/dailyreportuser/daily_infrastructure_report/data
report_dir = /home/dailyreportuser/daily_infrastructure_report/reports
```

Create the `data`, `reports`, and `logs` directories if they don't exist:

```bash
mkdir -p data reports logs
```

## 5. SSH Key Setup (Recommended)

For secure and automated access to target servers, set up SSH key-based authentication.

### 5.1. Generate SSH Key Pair (on reporting server)

If you don't already have one for `dailyreportuser`:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_dailyreport -C "dailyreportuser@reporting_server"
```

Follow the prompts. It's highly recommended to use a strong passphrase.

### 5.2. Copy Public Key to Target Servers

Copy the public key (`~/.ssh/id_ed25519_dailyreport.pub`) to each target server. Replace `your_ssh_user` and `target_server_ip` with actual values:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519_dailyreport.pub your_ssh_user@target_server_ip
```

If `ssh-copy-id` is not available, you can manually append the public key to `~/.ssh/authorized_keys` on the target server.

### 5.3. Test SSH Connectivity

Verify passwordless SSH access from the reporting server to each target server:

```bash
ssh -i ~/.ssh/id_ed25519_dailyreport your_ssh_user@target_server_ip
```

If successful, you should log in without a password (after entering the passphrase for `id_ed25519_dailyreport` if you set one).

## 6. Automation Setup (Cron Job)

Schedule the `run_daily_report.py` script to run daily using cron.

### 6.1. Open Crontab

As `dailyreportuser`:

```bash
crontab -e
```

### 6.2. Add Cron Entry

Add the following line to schedule the report for 6:00 AM daily. Ensure the paths are correct for your `dailyreportuser`.

```cron
0 6 * * * /home/dailyreportuser/daily_infrastructure_report/venv/bin/python3 /home/dailyreportuser/daily_infrastructure_report/scripts/run_daily_report.py >> /home/dailyreportuser/daily_infrastructure_report/logs/cron.log 2>&1
```

### 6.3. Save and Exit

Save the crontab file and exit the editor.

## 7. Verification

### 7.1. Manual Test Run

Execute the main script manually to ensure everything works as expected:

```bash
python3 scripts/run_daily_report.py
```

Check the console output for any errors. Verify that `data/` and `reports/` directories are populated with new files.

### 7.2. Check Logs

After the first scheduled cron run (or manual test), check the `cron.log` file for any errors or output:

```bash
cat logs/cron.log
```

### 7.3. Email Verification

Confirm that the recipient email addresses receive the reports. Check spam folders if necessary.

## 8. Conclusion

By following this deployment guide, you should have a fully functional and automated Daily Infrastructure Report system. Regular monitoring of logs and reports is recommended to ensure continuous operation and data accuracy. [1]

### 8.1. References

[1] Manus AI. (2025). *Daily Infrastructure Report Project Documentation*. [Internal Project Document].


