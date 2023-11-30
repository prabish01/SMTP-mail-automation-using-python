import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL, PASSWORD, RECEIVER_ID, SIGNATURE
import pandas as pd


# email credentials here

sender_id = EMAIL
sender_pass = PASSWORD
# receiver_id = RECEIVER_ID





# our message here

# msg = """\

# """

# Read csv file
readfile = pd.read_csv("list.csv")

for index, row in readfile.iterrows():
    name = row["Name"]
    room = row["Room no"]
    email = row["Email"]
    splitname = name.split()[0]

    message = MIMEMultipart('alternative')
    message["Subject"] = "Automation test 2"
    message["From"] = sender_id

    html = f"""\

    <html>
        <body>
        <p> Congratulations <b> {splitname} </b>!
        You have been selected for the automated testing of the system.
        Classes will be started from 12-01-2023 onwards.
        Your room is <b>{room}</b>
    
        Kindly enter your designated room.</p>
            
        {SIGNATURE}

        </body>
    </html>


    """



    html_MSG = MIMEText(html,"html")
    message.attach(html_MSG)


    # connect to gmail server and send

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as server:
            server.login(sender_id,sender_pass)
            server.sendmail(sender_id,email,message.as_string())
        print(f"Email sent successfully to {name} : {email} !!!")
        

    except Exception as e:
        print (f"Something went wrong... Couldn't send mail to {name}: {email}",e)

    # finally:
    #     server.quit()