from django.db import models
from datetime import datetime

# Create your models here.

class DVD(models.Model):
	genre = models.CharField(max_length = 255)
	title = models.CharField(max_length = 150)
	director_firstname = models.CharField(max_length = 150)
	director_lastname = models.CharField(max_length = 150)
	release_date = models.DateField(default = datetime.now())
	cast = models.CharField(max_length = 255)
	quantity = models.IntegerField()
	price = models.FloatField()
	dvd_cover1 = models.ImageField(upload_to = 'dvd', null = True)
	dvd_cover2 = models.ImageField(upload_to = 'dvd', null = True)
	dvd_cover3 = models.ImageField(upload_to = 'dvd', null = True)
	date_registered = models.DateField(default = datetime.now())

	class Meta:
		db_table = "DVD"