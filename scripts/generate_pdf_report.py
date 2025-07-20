from fpdf import FPDF
import json
import os
import configparser
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Daily Infrastructure Report", 0, 1, "C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 0, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, body)
        self.ln()

    def add_table(self, headers, data):
        self.set_font("Arial", "B", 10)
        col_width = self.w / (len(headers) + 1) # Adjust column width based on number of columns
        for header in headers:
            self.cell(col_width, 7, header, 1, 0, "C")
        self.ln()
        self.set_font("Arial", "", 8)
        for row in data:
            for item in row:
                self.cell(col_width, 6, str(item), 1, 0, "C")
            self.ln()
        self.ln(5)

def main():
    config = configparser.ConfigParser()
    config.read("/home/ubuntu/daily_infrastructure_report/config/config.ini")
    data_dir = config["PATHS"]["data_dir"]
    report_dir = config["PATHS"]["report_dir"]

    # Load data
    try:
        with open(os.path.join(data_dir, "running_servers.json"), "r") as f:
            running_servers_data = json.load(f)
        with open(os.path.join(data_dir, "disk_usage.json"), "r") as f:
            disk_usage_data = json.load(f)
        with open(os.path.join(data_dir, "user_logins.json"), "r") as f:
            user_logins_data = json.load(f)
        with open(os.path.join(data_dir, "system_uptime.json"), "r") as f:
            system_uptime_data = json.load(f)
    except FileNotFoundError as e:
        print(f"Error loading data: {e}. Please ensure data collection scripts have been run.")
        return

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # Running Servers
    pdf.chapter_title("1. Running Servers")
    pdf.chapter_body(f"Total running servers: {running_servers_data['count']}")
    if running_servers_data["servers"]:
        pdf.chapter_body("List of running servers: " + ", ".join(running_servers_data["servers"]))
    else:
        pdf.chapter_body("No servers reported as running.")

    # Disk Usage
    pdf.chapter_title("2. Disk Usage per Host")
    for host, disks in disk_usage_data.items():
        pdf.chapter_body(f"Host: {host}")
        headers = ["Filesystem", "Size", "Used", "Avail", "Use%", "Mounted On"]
        table_data = []
        for disk in disks:
            table_data.append([disk["filesystem"], disk["size"], disk["used"], disk["avail"], disk["use_percent"], disk["mounted_on"]])
        pdf.add_table(headers, table_data)

    # User Logins
    pdf.chapter_title("3. User Logins")
    for host, logins in user_logins_data.items():
        pdf.chapter_body(f"Host: {host}")
        successful_logins = [l for l in logins if l["status"] == "Success"]
        failed_logins = [l for l in logins if l["status"] == "Failed"]
        pdf.chapter_body(f"Successful logins: {len(successful_logins)}")
        pdf.chapter_body(f"Failed logins: {len(failed_logins)}")
        
        if logins:
            headers = ["Timestamp", "Username", "Source IP", "Status"]
            table_data = []
            for login in logins:
                table_data.append([login["timestamp"], login["username"], login["source_ip"], login["status"]])
            pdf.add_table(headers, table_data)

    # System Uptime
    pdf.chapter_title("4. System Uptime")
    for host, uptime in system_uptime_data.items():
        pdf.chapter_body(f"Host: {host} - Uptime: {uptime}")

    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    output_pdf_path = os.path.join(report_dir, f"infrastructure_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
    pdf.output(output_pdf_path)
    print(f"PDF report generated: {output_pdf_path}")

if __name__ == "__main__":
    main()


