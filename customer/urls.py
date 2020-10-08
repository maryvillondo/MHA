from django.urls import path
from . import views

# paths arranged alphabetically by name
app_name = 'customer'
urlpatterns = [
    # path('api/data', view.get_data, name='api-data'),

    # Test URL
    path('registration', views.CustomerRegView.as_view(), name='reg_view'),
    path('confirmation', views.CustomerConfirmationView.as_view(), name='confirmation_view'),
    
]
