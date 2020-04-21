"""swiggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from s_admin import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('',views.adminLogin, name='admin_login'),
    path('checkalogin/',views.cheakLogin,name='cheakLogin'),
    path('admin_home/',views.admin_home, name='admin_home'),
    path('admin_logout/',views.admin_logout, name='admin_logout'),




    # state
    path('open_state/', views.open_state, name='open_state'),
    path('save_state/',views.save_state,name='save_state'),
    path('update_state/',views.update_state,name='update_state'),
    path('update_state_data/',views.update_state_data,name='update_state_data'),
    path('delete_state/',views.delete_state,name='delete_state'),
    # city
    path('open_city/',views.open_city,name='open_city'),
    path('save_city/',views.save_city,name='save_city'),
    path('update_city/',views.update_city,name='update_city'),
    path('update_city_data/',views.update_city_data,name='update_city_data'),
    path('delete_city/',views.delete_city,name='delete_city'),
    # Area
    path('open_area/', views.open_area, name='open_area'),
    path('save_area/',views.save_area,name='save_area'),
    path('update_area/',views.update_area,name='update_area'),
    path('update_area_data/',views.update_area_data,name='update_area_data'),
    path('delete_area/',views.delete_area,name='delete_area'),
    # Type
    path('open_type/', views.open_type, name="open_type"),
    path('save_type/', views.save_type, name="save_type"),
    path('update_type/', views.update_type, name="update_type"),
    path('update_type_data/', views.update_type_data, name="update_type_data"),
    path('delete_type/', views.delete_type, name='delete_type'),

    # ============restaurant url =======================
    path('approved_rest/', views.approved_rest,name='approved_rest'),
    path('cancel_rest/', views.cancel_rest,name='cancel_rest'),
# ============restaurant show data url =======================
    path('show_approved_rest/', views.show_approved_rest,name='show_approved_rest'),
    path('show_cancel_rest/', views.show_cancel_rest,name='show_cancel_rest'),
    path('pending_rest/', views.pending_rest, name='pending_rest'),


]
