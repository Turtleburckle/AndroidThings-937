import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os

USERNAME = "your_email_address@gmail.com"
PASSWORD = "yourPassword"


def sendMail(to, subject, text, files):
    assert type(to) == list

    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, to, msg.as_string())
        server.quit()


sendMail(["Where_you_want_to_send_the_mail@gmail.com"],
         "The subject you want to appear!",
         "The message you want your mail to have!",
         ["root of the picture you want to send."])
