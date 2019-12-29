from django.db import models

from django.contrib.auth.models import User

# Create your models here
class Post(models.Model):
    name=models.CharField(max_length=200,default='False')
    password=models.CharField(max_length=300,default='0')
    rollno=models.CharField(max_length=200,default='0')
    collage=models.CharField(max_length=300,default='0')
    email=models.EmailField(max_length=500,default='0')
    male=models.BooleanField(default=0)
    female=models.BooleanField(default=0)
    def __str__(self):
        return self.name






