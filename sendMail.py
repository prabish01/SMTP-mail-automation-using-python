import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL, PASSWORD, RECEIVER_ID, SIGNATURE

# email credentials here

sender_id = EMAIL
sender_pass = PASSWORD
receiver_id = RECEIVER_ID


message = MIMEMultipart('alternative')
message["Subject"] = "Automation test"
message["From"] = sender_id
message["To"] = receiver_id


# our message here

msg = """\
 Your text here
"""
html = f"""\

{msg}

<html>
    <body>
        Your Signature and other texts
        {SIGNATURE}

    </body>
</html>


"""



html_MSG = MIMEText(html,"html")
message.attach(html_MSG)


# connect to gmail server and send

try:
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_id,sender_pass)

    server.sendmail(sender_id,receiver_id,message.as_string())
    print("Email sent successfully !!!")
    

except Exception as e:
    print ("Something went wrong...",e)

finally:
    server.quit()
