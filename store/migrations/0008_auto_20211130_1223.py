# Generated by Django 3.2.9 on 2021-11-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliveryaddress',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_no',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]