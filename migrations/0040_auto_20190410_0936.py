# Generated by Django 2.1.7 on 2019-04-10 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vishalapp', '0039_auto_20190410_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestdetails',
            name='Custid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
