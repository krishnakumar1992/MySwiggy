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
from restaurant import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.showMain, name="restro"),
    path('register/', views.registerPage, name="register"),
    path('save_rest/', views.save_res, name="save_rest"),
    path('resto_login/', views.resto_login, name="resto_login"),
    path('resto_login_cheack/', views.resto_login_cheack, name="resto_login_cheack"),
    path('restro_home/', views.restro_home, name="restro_home"),


    # ==================================under Retaurant=============================
    path('food_add/', views.food_add, name="food_add"),
    path('food_detail/', views.food_detail, name="food_detail"),
    path('food_update/<int:product_id>', views.food_update, name="food_update"),
    # path('food_update_success/', views.food_update_success, name="food_update_success"),
    path('Restro_logout/', views.Restro_logout, name="Restro_logout"),

]
