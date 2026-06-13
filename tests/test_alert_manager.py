import pytest
from src.alert_manager import AlertManager, AlertConfig
import socket

def test_send_alert(monkeypatch):
    def mock_smtp_ssl(*args, **kwargs):
        raise socket.gaierror(-3, "Temporary failure in name resolution")

    monkeypatch.setattr("smtplib.SMTP_SSL", mock_smtp_ssl)

    config = AlertConfig(
        sender_email="sender@example.com",
        sender_password="password",
        recipient_email="recipient@example.com",
        threshold=0.8,
    )
    alert_manager = AlertManager(config)
    cpu_usage = 0.9
    alert_manager.send_alert(cpu_usage)

def test_send_alert_no_error():
    config = AlertConfig(
        sender_email="sender@example.com",
        sender_password="password",
        recipient_email="recipient@example.com",
        threshold=0.8,
    )
    alert_manager = AlertManager(config)
    cpu_usage = 0.7
    alert_manager.send_alert(cpu_usage)
