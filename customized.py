import os
import smtplib
from email.message import EmailMessage
#use pip to install this library , python3 recommended

EMAIL_ADDRESS = 'YOUR-EMAIL-ADDRESS'
EMAIL_PASSWORD = 'YOUR-APP-PASSWORD'

msg =EmailMessage()
msg['Subject'] = 'SUBJECT-OF-EMAIL'
msg['From'] = EMAIL_ADDRESS

msg['To'] = 'RECIEVER-EMAIL'

#to send email to more than one recipient, use this
#contacts = ['first email','second email']
#msg['To'] = ', '. join(contacts)

msg.set_content('This is the plain text mail')

msg.add_alternative("""
<!DOCTYPE html>
<html>
    <body>
         <h1 style="color:SlateGray;">
         This is something creative with html , mail formatted well :D
         </h1>
        </body>
    </html>

""",subtype ='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
