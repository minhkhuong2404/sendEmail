import smtplib
import ssl
import datetime
import imapclient
import os
import weather, kenh14, NLD, VnExpress

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = imapclient.IMAPClient('imap.gmail.com', use_uid=True)
server.login("13156@student.vgu.edu.vn", os.envir.get(email_pass))

# select_info = server.select_folder('INBOX')
# print('%d messages in INBOX' % select_info[b'EXISTS'])
# UIDs = server.search('SINCE 05-Jan-2019')
# print(UIDs)

weather.call_weather()
kenh14.kenh14_news()
# VnExpress.VnExpress_news()
NLD.NLD_news()

subject = "Weather and Hot News Today"
body = "Email for the weather today and the next 7 days\nAlong the some hot news " \
       "today!\nHappy a good day!\n\n"
sender_email = "13156@student.vgu.edu.vn"
receiver_email = "khuonglu1999@gmail.com"
password = 'K8Zhe%+e'
# eoemtslwmzdabzuo
# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

weather = "weather.txt"  # In same directory as script
VnExpress = "VnExpress.txt"
NLD = "NLD.txt"
Kenh14 = "kenh14.txt"

# Open PDF file in binary mode
for filename in (weather, VnExpress, NLD, Kenh14):
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
