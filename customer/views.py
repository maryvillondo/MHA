from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import CustomerForm
from .models import *


# Create your views here.Arrange in alphabetical order
class CustomerIndexView(View):
    def get(self, request):
        qs_customer = Customer.objects.all();
        print(qs_customer)
        context = {
            'customers' : qs_customer
        }
        return render(request,'index.html',context)

    def post(self, request):
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
                # c_picture = request.FILES.get("customer-picture")# , customer_picture = c_picture                
                update_customer = Customer.objects.filter(person_ptr_id = cid).update(firstname = fname, middlename = mname, lastname = lname, street = street, barangay = barangay, city = city, province = province, zip_code = zip_code, country = country, birthdate = birthdate, status = status, gender = gender,spouse_fname = spouse_fname, spouse_mname = spouse_mname, spouse_lname = spouse_lname, spouse_occupation = spouse_occupation, no_children = no_children)
                print(update_customer)
                print('Update Successful')
            elif 'btnCDelete' in request.POST:
                print('Delete button clicked')
                cid = request.POST.get("dcustomer-id")
                customer = Customer.objects.filter(person_ptr_id=cid).delete()
                person = Person.objects.filter(id=cid).delete()
                print('Delete Successful')
        return HttpResponseRedirect("http://127.0.0.1:8000/customer/index")
 

class CustomerRegView(View):
    def get(self, request):
        # print('get')
        return render(request, 'CustomerRegistration.html')

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            #try
            fname = request.POST.get("firstname")
            mname = request.POST.get("middlename")
            lname = request.POST.get("lastname")
            street = request.POST.get("astreet")
            barangay = request.POST.get("abarangay")
            city = request.POST.get("acity")
            province = request.POST.get("aprovince")
            zip_code = request.POST.get("azip_code")
            country = request.POST.get("acountry")
            birthdate = request.POST.get("bdate")
            status = request.POST.get("cstatus")
            gender = request.POST.get("cgender")
            spouse_fname = request.POST.get("s_fname")
            spouse_mname = request.POST.get("s_mname")
            spouse_lname = request.POST.get("s_lname")
            spouse_occupation = request.POST.get("s_occupation")
            no_children = request.POST.get("numchildren")
            c_picture = request.FILES.get("customer_picture")
            form = Customer(firstname = fname, 
                            middlename = mname, 
                            lastname = lname, 
                            street = street, 
                            barangay = barangay, 
                            city = city, 
                            province = province, 
                            zip_code = zip_code, 
                            country = country, 
                            birthdate = birthdate, 
                            status = status, 
                            gender = gender, 
                            spouse_fname = spouse_fname, 
                            spouse_mname = spouse_mname, 
                            spouse_lname = spouse_lname, 
                            spouse_occupation = spouse_occupation, 
                            no_children = no_children, 
                            customer_picture = c_picture)
            form.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/customer/confirmation")
        else:
            print(form.errors)
            return HttpResponse('not valid')


class CustomerLandingView(View):
    def get(self, request):
        print('get')
        return render(request, 'LandingPage.html')

class CustomerConfirmationView(View):
    def get(self,request):
        print('get')
        return render(request, 'Confirmation.html')
