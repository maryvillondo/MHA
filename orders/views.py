from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect 
from customer.models import Customer
from orders.forms import OrderForm
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
	def post(self,request):
		form = OrderForm(request.POST)
		if form.is_valid():
			cust_id = request.POST.get("custID")	
			cust_name = request.POST.get("custName")
			dvdid = request.POST.get("dvdID")
			dvdtitle = request.POST.get("dvdTitle")
			movie_price = request.POST.get("dvd_price")
			quantity = request.POST.get("order_quantity")
			tprice = request.POST.get("totalprice")
			form = Order(customer_id=cust_id, customer_name=cust_name, dvd_id=dvdid, dvd_title=dvdtitle, items_ordered=quantity, total_price=tprice)
			form.save()
			return HttpResponse('order Saved')
		else:
			print(form.errors)
			return HttpResponse('not valid')
