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
    is_email_verified=models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='static/image/',null=True)
    objects=usermanager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email
    

from django.db import models

class Candidate(User):
    GENDER_TYPE = (
        ('NONE','None'),
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    )
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_TYPE,null=True,default='None')
    mobile = models.CharField(max_length=20,null=True,default='98')
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
    assigned_hr=models.ForeignKey('hrstaff',null=True,blank=True,on_delete=models.SET_NULL)

    

class hrstaff(User):
   autonumber=models.CharField(default='101',max_length=50,null=True)

class isselected(models.Model):
    candidate = models.ForeignKey(Candidate, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.candidate.email if self.candidate else 'No Candidate'

class employee(User):
    pass

# class status(models.Model):
#     candidate=models.ForeignKey(User,on_delete=models.CASCADE)
#     status=models.BooleanField(default=False);
#     verifier=models.ForeignKey(User,on_delete=models.CASCADE)
    


    
