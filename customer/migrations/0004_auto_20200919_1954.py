# Generated by Django 3.1.1 on 2020-09-19 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200919_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 9, 19, 19, 54, 40, 410317)),
        ),
    ]
