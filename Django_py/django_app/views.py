from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticalModel, Aliens
from django.views.generic import ListView



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


class AlienViews(ListView):
    model = Aliens
    template_name = 'django_app/alienview.html'
    context_object_name = 'aliens'
    queryset = Aliens.objects.filter(age__range = (1000, 2000))

class Artical(ListView):
    model = ArticalModel
    template_name = 'django_app/products.html'
    context_object_name = "products"