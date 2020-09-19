from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length = 100)
    middlename = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    barangay = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    zip_code = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    birthdate = models.DateField(default = datetime.now())
    status = models.CharField(max_length = 25)
    gender = models.CharField(max_length = 15)
    spouse_fname = models.CharField(max_length = 100)
    spouse_mname = models.CharField(max_length = 100)
    spouse_lname = models.CharField(max_length = 100)
    spouse_occupation = models.CharField(max_length =100)
    no_children = models.IntegerField()

    class Meta:
        db_table = "Person"

class Customer(Person):
    date_registered = models.DateField(default = datetime.now())
    customer_picture = models.BinaryField()

    class Meta:
        db_table = "Customer"
