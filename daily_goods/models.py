#coding=utf-8
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class GoodsType(models.Model):
    gtitle=models.CharField(max_length=20)
    is_delete=models.BooleanField(default=False)

    def __str__(self):
        return self.gtitle
class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=20)
    gpic=models.ImageField(upload_to='static/daily_goods')
    gprice=models.DecimalField(max_digits=6,decimal_places=2)
    is_delete=models.BooleanField(default=False)
    gunit=models.CharField(max_length=10)
    gclick=models.IntegerField()
    gdes=models.CharField(max_length=100)
    gstock=models.IntegerField()
    gdetail=HTMLField()
    grecommend = models.BooleanField(default=False)
    gtype=models.ForeignKey(GoodsType,on_delete=models.CASCADE,)

