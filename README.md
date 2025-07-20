# Automated-Daily-Infrastructure-Report-Scripts

# 🖥️ Automated Daily Infrastructure Report Scripts

A complete Python-based automation to collect, analyze, and report server infrastructure health. This project is perfect for sysadmins and DevOps engineers managing Linux environments.

> 🔗 GitHub: [https://github.com/chandugollavilli/Automated-Daily-Infrastructure-Report-Scripts](https://github.com/chandugollavilli/Automated-Daily-Infrastructure-Report-Scripts)

---

## 🔧 Features

- 📦 **Collects server metrics**:
  - Disk usage
  - Running server status
  - System uptime
  - User login activity

- 📄 **Report generation**:
  - PDF via FPDF
  - Excel via OpenPyXL

- ✉️ **Email notification**:
  - Sends reports to configured recipients (simulation enabled)

- 🧩 Modular & configurable through `config.ini`

---

## 🚀 Technologies Used

- Python 3.x
- FPDF (`generate_pdf_report.py`)
- OpenPyXL (`generate_excel_report.py`)
- ConfigParser for configurations
- Subprocess for automation

---

## 📁 Directory Structure

📂 Automated-Daily-Infrastructure-Report-Scripts/
├── collect_disk_usage.py
├── collect_running_servers.py
├── collect_system_uptime.py
├── collect_user_logins.py
├── generate_excel_report.py
├── generate_pdf_report.py
├── run_collection.py
├── run_daily_report.py
├── send_email.py
├── config/
│ └── config.ini
├── data/ # JSON outputs
├── reports/ # PDF/Excel reports
└── README.md

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/chandugollavilli/Automated-Daily-Infrastructure-Report-Scripts.git
cd Automated-Daily-Infrastructure-Report-Scripts

2️⃣ Install Requirements

pip install fpdf openpyxl

3️⃣ Configure Servers & Paths

[PATHS]
data_dir = ./data
report_dir = ./reports

[SERVERS]
server1 = user@192.168.1.10
server2 = user@192.168.1.11

[EMAIL]
smtp_username = your_email@example.com
recipient_emails = admin@example.com, devops@example.com

⚙️ Run the Report Automation

python run_daily_report.py

This will:

Collect all server data

Generate PDF & Excel reports

Simulate email notification

📤 Enable Real Emailing
To actually send emails, uncomment and configure the SMTP section in send_email.py.

👨‍💻 Author
Chandu Gollavilli
🔗 linkedin.com/in/chandragollavilli/
💬 Passionate about automation, DevOps, and creative problem-solving.

📜 License
This project is licensed under the MIT License.
