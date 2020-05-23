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
            request.session['status'] =True
            menu = RestaurantProduct.objects.filter(restro_name=uno)
            response=render(request,'restaurant/restro_home.html',{'res':res,'menu':menu})
            response.set_cookie('User_id',uno)
            return response


    except RestaurantModel.DoesNotExist:
        return render(request, 'restaurant/resto_login.html', {'loginForm': RestaurantLoginForm(),'error':'invalide login Id and password'})


def restro_home(request):
    id=request.COOKIES.get('User_id')
    data=RestaurantModel.objects.get(restro_contact=id)
    menu=RestaurantProduct.objects.filter(restro_name=id)
    return render(request,'restaurant/restro_home.html',{'res':data,'menu':menu})

# =============================under Restaurnat ======================================


def food_add(request):
    r_id=request.COOKIES.get('User_id')
    rf=productForm(request.POST,request.FILES)
    if rf.is_valid():
        db = rf.save(commit=False)
        db.restro_name = r_id
        db.save()
        return render(request,'restaurant/food_add.html',{'restro_id':r_id,'product':productForm()})
    else:
        return render(request,'restaurant/food_add.html',{'product':productForm()})


def food_detail(request):
    r_id = request.COOKIES.get('User_id')
    data=RestaurantProduct.objects.filter(restro_name=r_id)
    return render(request,'restaurant/food_detail.html',{'data':data})


def Restro_logout(request):
    request.session['status'] = False
    return redirect("resto_login")


def food_update(request,product_id):
    update=RestaurantProduct.objects.get(product_id=product_id)
    updatef_form = productForm(request.POST or None,request.FILES or None,instance=update)
    if updatef_form.is_valid():
        updatef_form.save()
        return redirect("food_detail")
    else:
        r_id = request.COOKIES.get('User_id')
        data = RestaurantProduct.objects.filter(restro_name=r_id)
        return render(request,'restaurant/food_detail.html',{'food_update':update,'data':data})


# def food_update_success(request):
#     # id=request.POST.get('restro_name')
#     # product_name=request.POST.get('product_name')
#     # product_quantity=request.POST.get('product_quantity')
#     # product_price=request.POST.get('product_price')
#     # product_discount=request.POST.get('product_discount')
#     # iproduct_statusd=request.POST.get('product_status')
#     # Product_img=request.POST.get('Product_img')
#     product_id=request.POST.get('restro_name')
#     update = RestaurantProduct.objects.get(restro_name=product_id)
#     updatef_form= productForm(request.POST,request.FILES,instance=update)
#     if updatef_form.is_valid():
#         updatef_form.save()
#         return render(request,'restaurant/food_detail.html')


 # sno = request.POST.get('s1')
 #    sname = request.POST.get('s2')
 #    Areamodel.objects.filter(Area_no=sno).update(Area_name=sname)
 #    return redirect('open_area')