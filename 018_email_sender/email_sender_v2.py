# password qwe576!sdf
# python@mrartful.com
# smtp: smtp.zone.eu port 465 SSL/TLS or 587 STARTTLS

import smtplib
from email.message import EmailMessage
smtp = smtplib.SMTP_SSL('smtp.zone.eu', 465)
smtp.login('python@mrartful.com', 'qwe576!sdf')

msg = EmailMessage()
msg['Subject'] = 'Sample email sent by Python'
msg['From'] = 'python@mrartful.com'
msg['To'] = 'sample@example.com'
msg.set_content('Sample mail sent by Python script. Have fun!')
msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <body>
                <h1 style="color: red;">What is in a lava lamp and how does it work?</h1>
                <p style="color: grey;">This is a test message sent to you by a small script on Python</p>
                <p style="color: grey;">The lamp contains blobs of coloured wax inside a glass vessel filled with clear or translucent liquid; the wax rises and falls as its density changes due to heating from an incandescent light bulb underneath the vessel. The appearance of the wax is suggestive of pāhoehoe lava, hence the name.</p>
            </body>
        </html>
        """, subtype='html')



smtp.send_message(msg)



