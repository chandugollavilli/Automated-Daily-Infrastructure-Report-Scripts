import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import configparser
import os
from datetime import datetime

def send_email(subject, body, to_emails, attachments=None):
    config = configparser.ConfigParser()
    config.read("/home/ubuntu/daily_infrastructure_report/config/config.ini")
    email_config = config["EMAIL"]

    from_email = email_config["smtp_username"]
    # from_password = email_config["smtp_password"]
    # smtp_server = email_config["smtp_server"]
    # smtp_port = int(email_config["smtp_port"])

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    if attachments:
        for attachment_path in attachments:
            if not os.path.exists(attachment_path):
                print(f"Attachment not found: {attachment_path}")
                continue
            
            part = MIMEBase("application", "octet-stream")
            with open(attachment_path, "rb") as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(attachment_path)}")
            msg.attach(part)

    # Simulate email sending
    print("\n--- Simulating Email Sending ---")
    print("To: " + msg["To"])
    print("From: " + msg["From"])
    print("Subject: " + msg["Subject"])
    print("Body:\n" + body)
    if attachments:
        print("Attachments:")
        for att in attachments:
            print("  - " + os.path.basename(att))
    print("--- Email Simulation Complete ---\n")
    return True

    # try:
    #     server = smtplib.SMTP(smtp_server, smtp_port)
    #     server.starttls()  # Secure the connection
    #     server.login(from_email, from_password)
    #     text = msg.as_string()
    #     server.sendmail(from_email, to_emails, text)
    #     server.quit()
    #     print("Email sent successfully!")
    #     return True
    # except Exception as e:
    #     print(f"Failed to send email: {e}")
    #     print("Please check your SMTP server settings, username, and password in config.ini.")
    #     return False

def main():
    config = configparser.ConfigParser()
    config.read("/home/ubuntu/daily_infrastructure_report/config/config.ini")
    report_dir = config["PATHS"]["report_dir"]
    recipient_emails = [email.strip() for email in config["EMAIL"]["recipient_emails"].split(",")]

    # Dummy attachments for testing
    # In a real scenario, these would be the actual generated reports
    today_str = datetime.now().strftime("%Y%m%d")
    # Find the latest generated PDF and Excel reports
    latest_pdf = None
    latest_excel = None
    
    report_files = sorted(os.listdir(report_dir), reverse=True)
    for f in report_files:
        if f.startswith(f"infrastructure_report_{today_str}") and f.endswith(".pdf"):
            latest_pdf = os.path.join(report_dir, f)
            break
    for f in report_files:
        if f.startswith(f"infrastructure_report_{today_str}") and f.endswith(".xlsx"):
            latest_excel = os.path.join(report_dir, f)
            break

    attachments = []
    if latest_pdf: attachments.append(latest_pdf)
    if latest_excel: attachments.append(latest_excel)

    subject = "Daily Infrastructure Report - " + datetime.now().strftime("%Y-%m-%d")
    body = "Please find attached the daily infrastructure report in PDF and Excel formats."

    if not attachments:
        print("No reports found to attach. Please ensure reports are generated.")
        return

    send_email(subject, body, recipient_emails, attachments)

if __name__ == "__main__":
    main()


