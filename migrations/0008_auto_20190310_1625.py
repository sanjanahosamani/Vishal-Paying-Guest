# Generated by Django 2.1.7 on 2019-03-10 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vishalapp', '0007_auto_20190310_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='state',
            new_name='State',
        ),
    ]
