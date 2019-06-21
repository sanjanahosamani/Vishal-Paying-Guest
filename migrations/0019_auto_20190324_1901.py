# Generated by Django 2.1.2 on 2019-03-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vishalapp', '0018_bookingdetails_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='bookid',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='paymode',
        ),
        migrations.AddField(
            model_name='payment',
            name='guestid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payamount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='paydate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='roomno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='custid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
