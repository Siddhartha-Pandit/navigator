import os
SENDER_EMAIL=os.environ.get('projectemail')
EMAIL_PASSWORD=os.environ.get('projectpass')
print(SENDER_EMAIL)
print(EMAIL_PASSWORD)