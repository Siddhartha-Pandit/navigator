from django.db import models

class candiate(models.Model):
    email=models.CharField(max_length=255,primary_key=True,unique=True,verbose_name=id)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)

    def __str__(self):
        return self.email

