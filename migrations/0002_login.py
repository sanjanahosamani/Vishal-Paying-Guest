# Generated by Django 2.1.7 on 2019-02-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vishalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Custid', models.CharField(max_length=50)),
                ('Custname', models.CharField(max_length=200)),
                ('Emailid', models.EmailField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Contactnumber', models.IntegerField(max_length=200)),
            ],
        ),
    ]
