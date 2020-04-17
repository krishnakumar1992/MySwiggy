from restaurant.models import *
from django import forms

class RestaurantForm(forms.ModelForm):
    rest_password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    class Meta:
        model=RestaurantModel
        fields="__all__"
        exclude=('rest_id','rest_otp','rest_statue',)