from django.shortcuts import render,redirect
from s_admin.models import AdminLoginModel
from django.contrib import messages
from s_admin.forms import *
from restaurant.models import RestaurantModel

# Create your views here.
def adminLogin(request):
    return render(request,"s_admin/login.html")


def cheakLogin(request):
    Uname=request.POST.get('admin_username')
    Upass=request.POST.get('admin_password')
    try:
        AdminLoginModel.objects.get(username=Uname,password=Upass)
        request.session['status']=True
        return render(request,'s_admin/admin_home.html')
    except AdminLoginModel.DoesNotExist:
        messages.error(request,'sorry invalide UserId and password')
        return redirect('admin_login')


def admin_home(request):
    return render(request,'s_admin/admin_home.html')


def admin_logout(request):
    request.session['status']=False
    return redirect('admin_login')


def open_state(request):
    return render(request,'s_admin/open_state.html',{'sf':StateForm(),'sdate':Statemodel.objects.all()})





def save_state(request):
    sf=StateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_state')
    else:
        return render(request,'s_admin/open_state.html',{'sf':sf})


def update_state(request):
    sno=request.GET.get('sno')
    sname=request.GET.get('name')
    data={'sno':sno,'sname':sname}
    return render(request,'s_admin/open_state.html',{'update_state':data,'sdate':Statemodel.objects.all()})


def update_state_data(request):
    sno=request.POST.get('s1')
    sname=request.POST.get('s2')
    Statemodel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('open_state')


def delete_state(request):
    sno = request.GET.get('sno')
    Statemodel.objects.filter(state_no=sno).delete()
    return redirect('open_state')

# city

def open_city(request):
    return render(request, 's_admin/open_city.html', {'sf': CityForm(), 'sdate': Citymodel.objects.all()})


def save_city(request):
    sf = CityForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_city')
    else:
        return render(request, 's_admin/open_city.html', {'sf': sf})


def update_city(request):
    sno = request.GET.get('sno')
    sname = request.GET.get('name')
    state=request.GET.get('State')
    data = {'sno': sno, 'sname': sname,'state':state}
    return render(request, 's_admin/open_city.html', {'update_city': data, 'sdate': Citymodel.objects.all()})

def update_city_data(request):
    sno = request.POST.get('s1')
    sname = request.POST.get('s2')
    Citymodel.objects.filter(City_no=sno).update(City_name=sname)
    return redirect('open_city')


def delete_city(request):
    sno = request.GET.get('sno')
    Citymodel.objects.filter(City_no=sno).delete()
    return redirect('open_city')

# Area
def open_area(request):
    return render(request,'s_admin/open_area.html',{'sf': AreaForm(), 'sdate': Areamodel.objects.all()})


def save_area(request):
    sf = AreaForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_area')
    else:
        return render(request, 's_admin/open_area.html', {'sf': sf})


def update_area(request):
    sno = request.GET.get('sno')
    sname = request.GET.get('name')
    area = request.GET.get('city')
    data = {'sno': sno, 'sname': sname, 'area': area}
    return render(request, 's_admin/open_area.html', {'update_city': data, 'sdate': Areamodel.objects.all()})


def update_area_data(request):
    sno = request.POST.get('s1')
    sname = request.POST.get('s2')
    Areamodel.objects.filter(Area_no=sno).update(Area_name=sname)
    return redirect('open_area')


def delete_area(request):
    sno = request.GET.get('sno')
    Areamodel.objects.filter(Area_no=sno).delete()
    return redirect('open_area')


# ================Restaurant Typy==========================
def open_type(request):
    return render(request,'s_admin/open_type.html',{"sf": RestaurantTypeForm(), "tdata": RestaurantTypeModel.objects.all()})

def save_type(request):
    sf = RestaurantTypeForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_type')
    else:
        return render(request, "s_admin/open_type.html", {"sf": sf})


def update_type(request):
    tno = request.GET.get("tno")
    tname = request.GET.get("tname")
    d1 = {"tno":tno,"tname":tname}
    return render(request,"s_admin/open_type.html",{"update_type":d1,"tdata":RestaurantTypeModel.objects.all()})

def update_type_data(request):
    tno = request.POST.get("t1")
    tname = request.POST.get("t2")
    RestaurantTypeModel.objects.filter(no = tno).update(type_name=tname)
    return redirect('open_type')


def delete_type(request):
    tno = request.GET.get("tno")
    RestaurantTypeModel.objects.filter(no=tno).delete()
    return redirect('open_type')

# =====================restaurant view ================================
def pending_rest(request):
    rs=RestaurantModel.objects.filter(restro_status='pending')
    return render(request,'s_admin/pending_rest.html',{'data':rs})


def approved_rest(request):
    rno=request.GET.get('rno')
    RestaurantModel.objects.filter(restro_id=rno).update(restro_status='approved')
    return redirect('admin_home')


def cancel_rest(request):
    rno = request.GET.get('rno')
    RestaurantModel.objects.filter(restro_id=rno).update(restro_status='cancel')
    return redirect('admin_home')


def show_approved_rest(request):
    rs = RestaurantModel.objects.filter(restro_status='approved')
    return render(request, 's_admin/show_approved_rest.html', {'data': rs})


def show_cancel_rest(request):
    rs = RestaurantModel.objects.filter(restro_status='cancel')
    return render(request, 's_admin/show_cancel_rest.html', {'data': rs})


