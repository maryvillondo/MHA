# Generated by Django 3.1.1 on 2020-09-17 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0008_auto_20200917_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 17, 14, 30, 9, 392586)),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 17, 14, 30, 9, 392586)),
        ),
    ]
