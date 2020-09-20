# Generated by Django 3.1.1 on 2020-09-16 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0004_auto_20200916_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='dvd',
            name='release_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
