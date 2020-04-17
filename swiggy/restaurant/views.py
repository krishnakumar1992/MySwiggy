from django.shortcuts import render,redirect
from restaurant.forms import *
from django.contrib import messages

# Create your views here.
def showmain(request):
    return render(request,'restaurant/main.html')


def register_page(request):
    return render(request,'restaurant/registration.html',{'rf':RestaurantForm(),})


def save_rest(request):
    rf=RestaurantForm(request.POST)

    if rf.is_valid():
        db=rf.save(commit=False)
        db.rest_otp = 5475
        db.rest_statue="pending"
        db.save()
        messages.success(request,"one admin approve the registraion reviee and email and text message")
        return redirect('resto')
    else:
        return render(request,'restaurant/registration.html',{'rf':rf})