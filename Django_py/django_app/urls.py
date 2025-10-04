# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')

from django_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('abc/', views.home, name= 'abc'),
    path("products/", views.products, name='products'),
    path('baseproducts/', views.baseproducts, name= 'baseproducts')
]