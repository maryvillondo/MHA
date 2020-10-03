from django.db import models
from datetime import datetime, date
import os

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
    birthdate = models.DateField()
    status = models.CharField(max_length = 25)
    gender = models.CharField(max_length = 15)
    spouse_fname = models.CharField(max_length = 100)
    spouse_mname = models.CharField(max_length = 100)
    spouse_lname = models.CharField(max_length = 100)
    spouse_occupation = models.CharField(max_length =100)
    no_children = models.IntegerField(default=0)

    class Meta:
        db_table = "Person"

def content_file_name(instance,filename):
    ext = filename.split('.')[-1]        
    filename = "%s.%s" % (instance.person_ptr_id, ext)
    return os.path.join('customer/',filename)

class Customer(Person):
    date_registered = models.DateField(auto_now_add=True)
    customer_picture = models.ImageField(upload_to = content_file_name, null = True, blank = True)

    class Meta:
        db_table = "Customer"
