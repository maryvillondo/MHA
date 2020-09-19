# Generated by Django 3.1.1 on 2020-09-15 16:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('barangay', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('birthdate', models.DateField(default=datetime.datetime(2020, 9, 16, 0, 44, 24, 385285))),
                ('status', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=15)),
                ('spouse_fname', models.CharField(max_length=100)),
                ('spouse_mname', models.CharField(max_length=100)),
                ('spouse_lname', models.CharField(max_length=100)),
                ('spouse_occupation', models.CharField(max_length=100)),
                ('no_childeren', models.IntegerField()),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customer.person')),
                ('date_registered', models.DateField(default=datetime.datetime(2020, 9, 16, 0, 44, 24, 385285))),
                ('customer_picture', models.BinaryField()),
            ],
            bases=('customer.person',),
        ),
    ]