# Generated by Django 3.1.1 on 2020-10-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateField(auto_now_add=True)),
                ('customer_id', models.CharField(max_length=5)),
                ('customer_name', models.CharField(max_length=250)),
                ('dvd_id', models.CharField(max_length=5)),
                ('dvd_title', models.CharField(max_length=250)),
                ('items_ordered', models.IntegerField()),
                ('total_price', models.FloatField()),
            ],
            options={
                'db_table': 'Order',
            },
        ),
    ]
