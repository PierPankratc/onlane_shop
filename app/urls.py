from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('sort/', views.price_sort, name='price_sort'),
    path('<slug:slug>', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>', views.product_details, name='product_details'),
]