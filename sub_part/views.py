from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def promo(request):
    return render(request,'promo.html')


#database register code 
def register_form_submission(request):
    if request.method=='POST':
        ex1=customer_register(first_name=request.POST.get('first_name'),
                             last_name=request.POST.get('last_name'),
                              email_id=request.POST.get('email_id'),
                              phone_number=request.POST.get('phone_number'))
        ex1.save()
        print("*****data saved successfully****")
        return render(request,'promo.html')
    else:
        print("*****data failed****")
        return render(request,'register.html')


def dashboard(request):
    return render(request,'dashboard.html')