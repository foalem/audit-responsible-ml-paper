import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, message, to_emails, smtp_server, smtp_port, smtp_user, smtp_pass):
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)

        for to_email in to_emails:
            # Create a separate email message for each recipient
            msg = MIMEMultipart()
            msg['From'] = smtp_user
            msg['To'] = to_email  # Set the current recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Send the email to the current recipient
            server.sendmail(smtp_user, to_email, msg.as_string())
            print(f"Email sent successfully to {to_email}")

        server.quit()
    except Exception as e:
        print(f"Email could not be sent. Error: {str(e)}")


# Read recipient emails from a CSV file
def read_recipient_emails_from_csv(csv_file):
    recipient_emails = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists
        for row in reader:
            recipient_email = row[1]  # Assuming the email is in the second column
            recipient_emails.append(recipient_email)
    return recipient_emails


# Example usage
if __name__ == "__main__":
    subject = "Invitation to Participate in Our ongoing Research on Logging Requirement for Audit"
    message = """Hello,


I hope this message finds you well. My name is FOALEM Patrick loic, and I'm a PhD student at SWAT Lab. We've noticed your contributions to machine learning projects on GitHub and would like to invite you to participate in a survey related to our ongoing research on Logging Requirement for Audit.


We understand the value of your expertise in this field, and your insights would greatly contribute to our study. Your responses will help us better understand current logging requirement for auditing machine learning based system.


The survey will take approximately 10 minutes of your time, and your input is highly valuable to us. We kindly request your participation and encourage you to share the survey link with any colleagues or contacts who are also involved in machine learning projects.


Please be assured that your privacy is a top priority for us. We have collected your email address from your GitHub contributions, and we will only send one reminder email after this initial invitation. If you choose not to participate, simply ignore these emails, and we won't send any further communication.


For added security, the survey will not request your name, and we will not log your IP address. We are committed to maintaining your anonymity throughout the survey.


To access the survey, please follow this link: https://docs.google.com/forms/d/e/1FAIpQLSfnWwfYJJXz8CqPk5VttKnQBZ_yh43vclYRLHV4pIw1Sjq6Og/viewform



Should you have any questions about the survey or our research, please don't hesitate to contact us. We appreciate your willingness to support our research and look forward to your valuable insights.


Best regards,

FOALEM Patrick loic

SWAT Lab., Polytechnique Montréal

C.P. 6079, succ. Centre-Ville

Montréal, QC, H3C 3A7, Canada"""

    to_emails = read_recipient_emails_from_csv("emails.csv")

    # SMTP server settings for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user1 = "fpatloic@gmail.com"
    smtp_user2 = "kagglecompet25@gmail.com"
    smtp_pass1 = "rqng qdrp vajd pegb"
    smtp_pass2 = "dfio yozt jfjx osau"
    smtp_user = "researchpaper0002@gmail.com"
    smtp_pass = "kjza zhmm xpjr xqnq"
    send_email(subject, message, to_emails, smtp_server, smtp_port, smtp_user, smtp_pass)
