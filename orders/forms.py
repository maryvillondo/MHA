from django import forms
from .models import *

class OrderForm(forms.ModelForm):
	
	class Meta:
		model = Order
		fields = ('customer_id','dvd_id')
