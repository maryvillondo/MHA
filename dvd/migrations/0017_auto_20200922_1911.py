# Generated by Django 3.1.1 on 2020-09-22 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0016_auto_20200922_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 22, 19, 11, 8, 708484)),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 22, 19, 11, 8, 708484)),
        ),
    ]
