# Generated by Django 3.1.1 on 2020-10-11 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvd', '0019_auto_20201009_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='release_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]