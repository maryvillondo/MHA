from django import forms
from .models import *

class DVDForm(forms.ModelForm):
	
	class Meta:
		model = DVD
		fields = ('title','quantity','price')