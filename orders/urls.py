from django.urls import path
from . import views

# paths arranged alphabetically by name
app_name = 'orders'
urlpatterns = [
    # Test URL
    path('', views.OrderTableView.as_view(), name='orders_view'),
    path('orderForm', views.OrderRegistrationView.as_view(), name='ordersreg_view')
]
