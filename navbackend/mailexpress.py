from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
import smtplib

def mailexpress(reciever,subject,body,attachments):
    SENDER_EMAIL='demoemailhw@gmail.com'
    EMAIL_PASSWORD='nbjhzxwxepyamsbv'
    msg=EmailMessage()
    msg['Subject']=subject
    msg['From']=SENDER_EMAIL
    msg['TO']=reciever
    msg.add_alternative(body,subtype='html')

    for attachment in attachments:
        with open(attachment, 'rb') as f:
            file_data = f.read()
            file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(SENDER_EMAIL,EMAIL_PASSWORD)
        smtp.send_message(msg)
        

