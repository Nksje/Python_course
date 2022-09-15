import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# MIME - Multipurpose Internet Mail Extension
# Here just add a SMTP details of your server
with smtplib.SMTP('smtp.zone.eu', 587) as server:
    # .ehlo() identifies sever we are using
    server.ehlo()
    # Traffic encryption
    server.starttls()
    server.ehlo()
    # Next, log in to the server
    server.login("python@mrartful.com", "qwe576!sdf")

    msg = MIMEMultipart()
    msg['From'] = "python@mrartful.com"
    msg['To'] = "someone@example.com"
    msg['Subject'] = "Python email"
    body = "Python test mail sent: " + str(datetime.now())
    body2 = f"<h1>Hello World</h1>" \
            f"<p style='color: red;'>Hello people of Earth!</p>" \
            f"<p style='color: green;'>{str(datetime.now())}</p>"
    # msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(body2, 'html'))
    text = msg.as_string()

    # Send the mail
    # msg = "Hello!" # The /n separates the message from the headers
    server.sendmail("python@mrartful.com", "someone@example.com", text)


