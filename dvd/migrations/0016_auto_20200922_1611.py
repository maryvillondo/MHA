# Generated by Django 3.1.1 on 2020-09-22 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0015_auto_20200919_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 22, 16, 11, 58, 662664)),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 22, 16, 11, 58, 662664)),
        ),
    ]