from django.urls import path
from . import views

# paths arranged alphabetically by name
app_name = 'dashboard'
urlpatterns = [
    # Test URL
    path('index', views.DashboardIndexView.as_view(), name='index_view'),
    path('', views.LandingView.as_view(), name='landing_view')
]
