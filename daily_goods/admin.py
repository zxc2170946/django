from django.contrib import admin
from .models import *
# Register your models here.
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display=['id','gtitle']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display=['id','gtitle','gprice','gunit','gstock','gdetail','gtype']
admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)