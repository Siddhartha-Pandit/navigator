import smtplib
import imghdr
from email.message import EmailMessage  #formatting email
EMAIL_ADDRESS='demoemailhw@gmail.com'
EMAIL_PASSWORD='nbjhzxwxepyamsbv'

contacts=['siddharthapandit66@gmail.com','connect2ranjitsingh@gmail.com']
msg=EmailMessage()
msg['Subject']='This is subject'
msg['From']=EMAIL_ADDRESS
# msg['TO']='connect2ranjitsingh@gmail.com'  this is for single user
msg['TO']=','.join(contacts)
msg.set_content('This is body section of email')
msg.add_alternative("""\
          <!DOCTYPE html>
                    <html>
                    <body>
                    <h1>This is for html email</h1>
                    </body>
                    </html>

                    """,subtype='html')

files =['navbackend\\a.jpg','navbackend\\k.docx','navbackend\\k.pdf','navbackend\\k.xls']
for file in files:
    with open(file,'rb') as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)  #return the type of mail we need only for image
        file_name=f.name
    
    #    .                       maintype=application for pdf and subtype=octet-stream for pdf                             
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:  #already connection established
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)#loginmethod
    subject='This is my subject'
    body='This is my mail body'
    # msg=f'Subjects: {subject}\n\n{body}'
   
    EMAIL_RECIEVER='connect2ranjitsingh@gmail.com'
    smtp.send_message(msg)
# with smtplib.SMTP('smtp.gmail.com',587) as smtp:
#                     #mail server    port that we want to connect with
#     smtp.ehlo()   #ehlo method used to identify with mail severthat we are using
#     smtp.starttls()  ##ecnrypt in the traffic
#     smtp.ehlo()  ##reidentify as encrypted connection
#     smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)#loginmethod
#     subject='This is my subject'
#     body='This is my mail body'
#     msg=f'Subjects: {subject}\n\n{body}'
   
#     EMAIL_RECIEVER='connect2ranjitsingh@gmail.com'
#     smtp.sendmail(EMAIL_ADDRESS,EMAIL_RECIEVER,msg)