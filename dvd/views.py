from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import DVDForm
from .models import *
from datetime import datetime

# Create your views here.
# class DVDIndexView(View):
# 	def get(self, request):
# 		qs_dvds = DVD.objects.all()	
# 		context = {
# 			'dvds' : qs_dvds
# 		}
# 		return render(request, 'index.html', context)
# 	def post(self, request):
# 		if request.method == 'POST':	
# 			if 'btnUpdate' in request.POST:	
# 				sku = request.POST.get("sku")
# 				genrelist = request.POST.getlist("genre")
# 				genre = ','.join(genrelist)
# 				title = request.POST.get("title")
# 				director_firstname = request.POST.get("director_firstname")
# 				director_lastname = request.POST.get("director_lastname")
# 				release_date = request.POST.get("release_date")
# 				cast = request.POST.get("cast")
# 				quantity = request.POST.get("quantity")
# 				price = request.POST.get("price")
# 				# dvd_cover1 = request.FILES.get("dvd_cover1")
# 				# dvd_cover2 = request.FILES.get("dvd_cover2")
# 				# dvd_cover3 = request.FILES.get("dvd_cover3")
# 				update_dvd = DVD.objects.filter(id = sku).update(genre = genre, 
# 																	title = title, 
# 																	director_firstname = director_firstname, 
# 																	director_lastname = director_lastname, 
# 																	release_date = release_date,
# 																	cast = cast, 
# 																	quantity = quantity, 
# 																	price = price)
# 				# if dvd_cover1 is not None:
# 				# 	update_dvd_cover1 = DVD.objects.filter(id = sku).update(dvd_cover1 = dvd_cover1)
# 				# if dvd_cover2 is not None:
# 				# 	update_dvd_cover2 = DVD.objects.filter(id = sku).update(dvd_cover2 = dvd_cover2)
# 				# if dvd_cover3 is not None:
# 				# 	update_dvd_cover3 = DVD.objects.filter(id = sku).update(dvd_cover3 = dvd_cover3)
# 			elif 'btnDelete' in request.POST:	
# 				sku = request.POST.get("sku")
# 				dvd = DVD.objects.filter(id = sku).delete()
# 		#return HttpResponse ('post')
# 		return redirect('dashboard:dvd_index_view')

class DVDRegistrationView(View):
	def get(self, request):
		return render(request, 'DVDRegistration.html')
	def post(self, request):	
		form = DVDForm(request.POST or None, request.FILES or None)		
		if form.is_valid():
			# try:
			genrelist = request.POST.getlist("genre")
			genre = ','.join(genrelist)
			title = request.POST.get("title")
			director_firstname = request.POST.get("director_firstname")
			director_lastname = request.POST.get("director_lastname")
			release_date = request.POST.get("release_date")
			cast = request.POST.get("cast")
			quantity = request.POST.get("quantity")
			price = request.POST.get("price")
			dvd_cover1 = request.FILES.get("dvd_cover1")
			dvd_cover2 = request.FILES.get("dvd_cover2")
			dvd_cover3 = request.FILES.get("dvd_cover3")
			date_registered = datetime.now()

			form = DVD(genre = genre, 
						title = title, 
						director_firstname = director_firstname, 
						director_lastname = director_lastname, 
						release_date = release_date,
						cast = cast, 
						quantity = quantity, 
						price = price, 
						dvd_cover1 = dvd_cover1, 
						dvd_cover2 = dvd_cover2, 
						dvd_cover3 = dvd_cover3,
						date_registered = date_registered)
			form.save()

			return HttpResponse('DVD record saved!')			
			# return render(request,'successpage.html')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('not valid')			