# Generated by Django 2.1.7 on 2019-02-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=200)),
                ('Lname', models.CharField(max_length=200)),
                ('Emailid', models.EmailField(max_length=200)),
                ('NewPassword', models.CharField(max_length=200)),
                ('ConfirmPassword', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
    ]
