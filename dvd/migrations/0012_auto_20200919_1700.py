# Generated by Django 3.1.1 on 2020-09-19 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0011_auto_20200917_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 19, 17, 0, 54, 788649)),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 19, 17, 0, 54, 788649)),
        ),
    ]