import smtplib
from email.message import EmailMessage
from dataclasses import dataclass
import socket

@dataclass
class AlertConfig:
    sender_email: str
    sender_password: str
    recipient_email: str
    threshold: float

class AlertManager:
    def __init__(self, config):
        self.config = config

    def send_alert(self, cpu_usage):
        if cpu_usage > self.config.threshold:
            msg = EmailMessage()
            msg.set_content(f"CPU usage exceeded {self.config.threshold}%")
            msg["Subject"] = "CPU Usage Alert"
            msg["From"] = self.config.sender_email
            msg["To"] = self.config.recipient_email
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(self.config.sender_email, self.config.sender_password)
                    smtp.send_message(msg)
            except socket.gaierror as e:
                print(f"Error sending alert: {e}")

def main():
    config = AlertConfig(
        sender_email="sender@example.com",
        sender_password="password",
        recipient_email="recipient@example.com",
        threshold=0.8,
    )
    alert_manager = AlertManager(config)
    cpu_usage = 0.9  # Replace with actual CPU usage
    alert_manager.send_alert(cpu_usage)

if __name__ == "__main__":
    main()
