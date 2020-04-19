from django.shortcuts import render,redirect
from restaurant.forms import *
from django.contrib import messages
from restaurant.models import *

from restaurant.forms import RestaurantForm,RestaurantLoginForm


def showMain(request):
    return render(request,"Restaurant/main.html")


def registerPage(request):
    return render(request,"restaurant/registration.html",{"rf":RestaurantForm()})


def save_res(request):
    rf = RestaurantForm(request.POST)
    if rf.is_valid():
        db = rf.save(commit=False)
        db.restro_otp = 5475
        db.restro_status = 'pending'
        db.save()
        messages.success(request,"Once the admin approve the Registration you will receive an email and a text Message")
        return redirect('restro')
    else:
        return render(request,"restaurant/registration.html",{"rf":rf})


def resto_login(request):
    return render(request,'restaurant/resto_login.html',{'loginForm':RestaurantLoginForm()})


def resto_login_cheack(request):
    uno=request.POST.get('contact_no')
    upass=request.POST.get('password')
    try:
        res=RestaurantModel.objects.get(restro_contact=uno,restro_password=upass)
        if res.restro_status =='pending':
            message="hello Restaurant "+res.restro_name+"Your Registration still need Pending"
            return render(request, 'restaurant/resto_login.html',{'loginForm': RestaurantLoginForm(), 'error':message})
        elif res.restro_status=='cancel':
            message = "hello Restaurant " + res.restro_name + "Your Registration still need Cancel"
            return render(request, 'restaurant/resto_login.html',{'loginForm': RestaurantLoginForm(), 'error': message})
        else:
            request.session['status'] = True
            return redirect('restro_home')


    except RestaurantModel.DoesNotExist:
        return render(request, 'restaurant/resto_login.html', {'loginForm': RestaurantLoginForm(),'error':'invalide login Id and password'})


def restro_home(request):
    return render(request,'restaurant/restro_home.html')