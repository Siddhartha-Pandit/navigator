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

    objects=usermanager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email
    

class candidate(User):
    pass

class hrstaff(User):
    pass

class employee(User):
    pass

    
