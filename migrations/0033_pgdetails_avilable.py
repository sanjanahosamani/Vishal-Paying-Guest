# Generated by Django 2.1.7 on 2019-04-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vishalapp', '0032_auto_20190408_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='pgdetails',
            name='avilable',
            field=models.CharField(default='False', max_length=5),
        ),
    ]