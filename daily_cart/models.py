#coding=utf-8

from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user=models.ForeignKey('daily_user.UserInfo',on_delete=models.CASCADE,)
    goods=models.ForeignKey('daily_goods.GoodsInfo',on_delete=models.CASCADE,)
    count=models.IntegerField(default=0)