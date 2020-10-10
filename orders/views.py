from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect 
from customer.models import Customer
from customer.forms import CustomerForm
from dvd.models import DVD
from dvd.forms import DVDForm
from datetime import datetime


# Create your views here.
class OrderTableView(View):
    def get(self, request):
        print('get')
        return render(request, 'Order_Dashboard.html')

class OrderRegistrationView(View):
	def get(self, request):
		qs_customer = Customer.objects.all()
		qs_dvds = DVD.objects.all()
		print(qs_customer)
		print(qs_dvds)
		context = {
			'customers' : qs_customer,
			'dvds' : qs_dvds
		}
		return render(request,'OrderForm.html',context)
			