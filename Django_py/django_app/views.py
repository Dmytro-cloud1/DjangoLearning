from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    mess_dict = {"message":"ABCD", "products":['apples', 'bananas']}
    return render(request, 'django_app/main.html', context= mess_dict)


