from django.urls import path
from . import views

# paths arranged alphabetically by name
app_name = 'customer'
urlpatterns = [
    # path('api/data', view.get_data, name='api-data'),

    # Test URL
    path('index', views.CustomerIndexView.as_view(), name='index_view'),
    path('registration', views.CustomerRegView.as_view(), name='reg_view'),
    path('landing', views.CustomerLandingView.as_view(), name='landing_view'),
]