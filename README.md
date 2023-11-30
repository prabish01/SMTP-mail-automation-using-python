# SMTP-mail-automation-using-python
This repository contains a Python script for sending automated emails using the SMTP protocol. The script utilizes the smtplib library for email server communication and email.mime modules for creating MIME-formatted messages.


## Key Features:

### Separation of Credentials:

Sensitive information such as email credentials is stored in a separate configuration file (`config.py`) to enhance security. The file is added to the `.gitignore` list to ensure it is not pushed to the repository.

### HTML Email Content:

The email message includes an HTML version for a visually rich experience. Both plain text and HTML versions are attached using `MIMEMultipart` and `MIMEText` classes.

Usage:
Create a config.py file with your email credentials:

### config.py
In config.py file add the following EMAIL, PASSWORD, RECEIVER_ID and SIGNATURE

EMAIL = "your_email@example.com"
PASSWORD = "your_password"
RECEIVER_ID = "receiverid@gmail.com"
SIGNATURE = "signature either in plain text or if you use html then replace "" with f"""\  """  " 

Run the your_mail_script.py file to send automated emails.



