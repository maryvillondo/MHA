from django.urls import path
from . import views

app_name = 'dvd'
urlpatterns = [
	path('index', views.DVDIndexView.as_view(), name="index_view"),
	path('registration', views.DVDRegistrationView.as_view(), name="registration_view"),
] 

