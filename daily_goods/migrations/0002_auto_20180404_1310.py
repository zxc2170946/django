# Generated by Django 2.0.3 on 2018-04-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='static/daily_goods'),
        ),
    ]
