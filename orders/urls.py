from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment/<int:order_id>/', views.dummy_payment, name='dummy_payment'),
    path('success/', views.order_success, name='order_success'),
    path('my-orders/', views.my_orders, name='my_orders'),
]

