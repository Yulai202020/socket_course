import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525)

server.ehlo()
server.login("2656be95a002b8", "66bd35f7c7c88f")


# send message text
msg = MIMEMultipart()
msg["From"] = "meeee"
msg["To"] = input("Enter to: ")
msg["Subject"] = input("Enter subject: ")

msg.attach(MIMEText("hi", 'plain'))

# send picture

filename = '/home/yulai/Downloads/MainAfter.avif'

attachment = open(filename, "rb")

p = MIMEBase('application', 'octet-streamE')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={filename}")

# send full message

text = msg.as_string()
server.sendmail('ngmyulai@gmail.com', "2656be95a002b8@mailtrap.io", text)