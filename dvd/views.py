from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class DVDIndexView(View):
	def get(self, request):
		#print('get')
		return render(request, 'index.html')
	def post(self, request):
		return render(request, 'DVDRegistration.html')

class DVDRegistrationView(View):
	def get(self, request):
		return render(request, 'DVDRegistration.html')			