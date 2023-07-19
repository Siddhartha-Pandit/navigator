from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import usermanager
class User(AbstractUser):
    USER_TYPE=(
        ('candidate','Candidate'),
        ('hr','Hr'),
        ('employee','Employee'),
    )
    username=None
    email=models.EmailField(primary_key=True,unique=True)
    user_type=models.CharField(max_length=20,choices=USER_TYPE)
    is_email_verified=models.BooleanField(default=True)
    objects=usermanager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email
    

from django.db import models

class Candidate(User):
    GENDER_TYPE = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    )
    profile_image = models.ImageField(upload_to='static/image/',null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_TYPE,null=True)
    mobile = models.CharField(max_length=20,null=True,default='')
    nationality = models.CharField(max_length=50,null=True,default='')
    temporaryaddress = models.CharField(max_length=500,null=True,default='')
    permanentaddress = models.CharField(max_length=500,null=True,default='')
    bachelor_institute = models.CharField(max_length=100, null=True,default='')
    bachelor_marks = models.IntegerField(null=True,default=0)
    bachelor_transcript = models.FileField(upload_to='static/files',null=True)
    plus_two_institute = models.CharField(max_length=100,null=True,default='')
    plus_two_marks = models.IntegerField(null=True,default=0)
    plus_two_transcript = models.FileField(upload_to='static/files',null=True)
    see_institute = models.CharField(max_length=100,null=True,default='')
    see_marks = models.IntegerField(null=True,default=0)
    see_transcript = models.FileField(upload_to='static/files',null=True)
    technical_skills = models.CharField(max_length=500,null=True,default='')
    project = models.CharField(max_length=500,null=True,default='')
    internsip = models.CharField(max_length=500,null=True,default='')
    awards = models.CharField(max_length=500, null=True,default='')
    refrence_name_1 = models.CharField(max_length=30,null=True,default='')
    refrence_email_1 = models.EmailField(null=True,default='')
    refrence_phone_1 = models.CharField(max_length=20,null=True,default='')
    refrence_name_2 = models.CharField(max_length=30,null=True,default='')
    refrence_email_2 = models.EmailField(null=True,default='')
    refrence_phone_2 = models.CharField(max_length=20,null=True,default='')

    


class hrstaff(User):
    pass

class employee(User):
    pass

    
