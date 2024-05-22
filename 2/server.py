import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.world4you.com', 25)

server.ehlo()

server.login("mail@mail.com", "password123")

msg = MIMEMultipart()