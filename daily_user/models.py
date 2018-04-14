#coding=utf-8
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=20)
    pwd=models.CharField(max_length=40)
    email=models.CharField(max_length=20)
    shou=models.CharField(max_length=50,default='')
    uadr=models.CharField(max_length=50,default='')
    post=models.CharField(max_length=6,default='')
    tel=models.CharField(max_length=11,default='')



