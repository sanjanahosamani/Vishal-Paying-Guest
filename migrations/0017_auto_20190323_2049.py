# Generated by Django 2.1.7 on 2019-03-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vishalapp', '0016_pgdetails_room_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingdetails',
            name='cost',
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='totcost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
