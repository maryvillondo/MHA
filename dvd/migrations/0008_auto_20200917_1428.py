# Generated by Django 3.1.1 on 2020-09-17 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0007_auto_20200917_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 17, 14, 28, 4, 820924)),
        ),
    ]