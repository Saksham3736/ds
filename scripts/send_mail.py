"""
GNE'S APEX 2026 — Automated Email Dispatch Script
==================================================
Sends the responsive HTML invitation email with attached 'Apex-2026-brochure.pdf'.
Supports Gmail SMTP (using App Passwords), Outlook, or custom institutional SMTP servers.

Usage:
  python scripts/send_mail.py --to recipient@school.edu.in --subject "You Are Cordially Invited to GNE'S APEX 2026 | GNDEC Ludhiana"
"""

import os
import sys
import smtplib
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_invitation_email(
    to_email,
    subject="You Are Cordially Invited to GNE'S APEX 2026 | GNDEC Ludhiana",
    sender_email=None,
    sender_password=None,
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    attach_brochure=True,
    html_file="index-embedded.html"
):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    html_path = os.path.join(base_dir, html_file)
    pdf_path = os.path.join(base_dir, "Apex-2026-brochure.pdf")

    if not os.path.exists(html_path):
        print(f"Error: HTML template not found at {html_path}")
        return False

    # Read HTML content
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Create root multipart message
    msg = MIMEMultipart('mixed')
    msg['From'] = f"GNE'S APEX 2026 <{sender_email}>" if sender_email else "GNE'S APEX 2026"
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach HTML body
    msg_html = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(msg_html)

    # Attach Brochure PDF if requested
    if attach_brochure and os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename="Apex-2026-brochure.pdf")
            msg.attach(pdf_attachment)
            print(f"Attached brochure: Apex-2026-brochure.pdf ({round(os.path.getsize(pdf_path)/(1024*1024), 2)} MB)")

    if not sender_email or not sender_password:
        print("\n--- DRY RUN MODE (No SMTP credentials provided) ---")
        print(f"Target Recipient: {to_email}")
        print(f"Subject: {subject}")
        print(f"HTML Template: {html_file}")
        print("To send live emails, set environment variables SENDER_EMAIL and SENDER_PASS or pass arguments.")
        return True

    # Live sending via SMTP
    try:
        print(f"\nConnecting to {smtp_server}:{smtp_port}...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"Successfully dispatched invitation email to {to_email}!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Send APEX 2026 Invitation Email")
    parser.add_argument('--to', default=os.getenv('RECIPIENT_EMAIL', 'test@example.com'), help="Recipient email address")
    parser.add_argument('--subject', default="You Are Cordially Invited to GNE'S APEX 2026 | GNDEC Ludhiana", help="Email subject")
    parser.add_argument('--sender', default=os.getenv('SENDER_EMAIL'), help="Sender email address")
    parser.add_argument('--password', default=os.getenv('SENDER_PASS'), help="Sender email/app password")
    parser.add_argument('--server', default="smtp.gmail.com", help="SMTP server host")
    parser.add_argument('--port', type=int, default=587, help="SMTP port")
    parser.add_argument('--template', default="index-embedded.html", help="HTML template file to send")

    args = parser.parse_args()
    send_invitation_email(
        to_email=args.to,
        subject=args.subject,
        sender_email=args.sender,
        sender_password=args.password,
        smtp_server=args.server,
        smtp_port=args.port,
        html_file=args.template
    )
