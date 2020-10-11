from django.db import models
from datetime import datetime, date
from dvd.models  import DVD
from customer.models import Customer

# Create your models here.
class Order (models.Model):
	date_ordered = models.DateField(auto_now_add = True)
	customer_id = models.CharField(max_length = 5)
	customer_name = models.CharField(max_length = 250)
	dvd_id = models.CharField(max_length = 5)
	dvd_title =  models.CharField(max_length = 150)
	items_ordered = models.IntegerField()
	total_price = models.FloatField()

	class Meta:
		db_table = "Order"