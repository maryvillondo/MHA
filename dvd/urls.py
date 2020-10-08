from django.urls import path
from . import views

app_name = 'dvd'
urlpatterns = [
	# path('index', views.DVDIndexView.as_view(), name="dvd_index_view"),
	path('registration', views.DVDRegistrationView.as_view(), name="dvd_registration_view"),
] 
