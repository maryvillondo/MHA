# Generated by Django 3.1.1 on 2020-09-15 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200916_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 16, 2, 40, 12, 996124)),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 9, 16, 2, 40, 12, 995125)),
        ),
    ]
