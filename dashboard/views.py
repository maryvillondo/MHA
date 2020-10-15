from django.http import Http404
from django.views.generic import View
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect 
from customer.models import Customer,Person
from customer.forms import CustomerForm
from dvd.models import DVD
from dvd.forms import DVDForm
from datetime import datetime

# Create your views here.
class DashboardIndexView(View):
	def get(self, request):
		qs_customer = Customer.objects.all()
		qs_dvds = DVD.objects.all()
		print(qs_customer)
		print(qs_dvds)
		context = {
			'customers' : qs_customer,
			'dvds' : qs_dvds
		}
		return render(request,'index.html',context)

	def post(self,request):
		if request.method == 'POST':
			if 'btnCUpdate' in request.POST:
				print ('Update button button clicked')
				cid = request.POST.get("customer-id")
				fname = request.POST.get("customer-fname")
				mname = request.POST.get("customer-mname")
				lname = request.POST.get("customer-lname")
				street = request.POST.get("customer-street")
				barangay = request.POST.get("customer-barangay")
				city = request.POST.get("customer-city")
				province = request.POST.get("customer-province")
				zip_code = request.POST.get("customer-zip")
				country = request.POST.get("customer-country")
				birthdate = request.POST.get("customer-bdate")
				status = request.POST.get("customer-status")
				gender = request.POST.get("customer-gender")
				spouse_fname = request.POST.get("s-fname")
				spouse_mname = request.POST.get("s-mname")
				spouse_lname = request.POST.get("s-lname")
				spouse_occupation = request.POST.get("s-occupation")
				no_children = request.POST.get("num-children")            
				update_customer = Customer.objects.filter(person_ptr_id = cid).update(firstname = fname, middlename = mname, lastname = lname, street = street, barangay = barangay, city = city, province = province, zip_code = zip_code, country = country, birthdate = birthdate, status = status, gender = gender,spouse_fname = spouse_fname, spouse_mname = spouse_mname, spouse_lname = spouse_lname, spouse_occupation = spouse_occupation, no_children = no_children)
				print(update_customer)
				print('Customer Update Successful')
			elif 'btnUpdate' in request.POST:	
				sku = request.POST.get("sku")
				genrelist = request.POST.getlist("genre")
				genre = ','.join(genrelist)
				title = request.POST.get("title")
				director_firstname = request.POST.get("director_firstname")
				director_lastname = request.POST.get("director_lastname")
				release_date = request.POST.get("release_date")
				cast = request.POST.get("cast")
				quantity = request.POST.get("quantity")
				price = request.POST.get("price")
				update_dvd = DVD.objects.filter(id = sku).update(genre = genre, title = title, director_firstname = director_firstname, director_lastname = director_lastname, release_date = release_date, cast = cast, quantity = quantity, price = price)
				print(update_dvd)
				print('DVD Update Successful')
			elif 'btnDelete' in request.POST:	
				sku = request.POST.get("sku")
				dvd = DVD.objects.filter(id = sku).delete()
				print('Delete Successful')
			elif 'btnCDelete' in request.POST:
				print('Delete button clicked')
				cid = request.POST.get("dcustomer-id")
				customer = Customer.objects.filter(person_ptr_id=cid).delete()
				person = Person.objects.filter(id=cid).delete()
				print('Delete Successful')
		return HttpResponseRedirect("http://127.0.0.1:8000/index")

class LandingView(View):
    def get(self, request):
        print('get')
        return render(request, 'LandingPage.html')

class ConfirmationView(View):
    def get(self,request):
        print('get')
        return render(request, 'Confirmation.html')