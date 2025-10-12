from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticalModel, Aliens

# Create your views here.
def home(request):
    mess_dict = {"message":"ABCD", "products":['apples', 'bananas']}
    return render(request, 'django_app/main.html', context= mess_dict)


#cost title discription
def products(request):
    context = {"products":[{
        'title':"srawberry",
        'cost': 100,
        'discription':'fresh'
    },
    {
        'title':"bananas",
        'cost': 50,
        'discription':'yellow'
    }]}
    return render(request, 'django_app/index.html', context= context)

def aliens(request):
    alien = Aliens.objects.all()
    return render(request, 'django_app/main.html', context= {"aliens": alien})

def baseproducts(request):
    products = ArticalModel.objects.all()
    return render(request, 'django_app/products.html', context={"products":products})