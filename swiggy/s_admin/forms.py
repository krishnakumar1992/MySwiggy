from django import forms
from s_admin.models import Statemodel,Citymodel,Areamodel,RestaurantTypeModel

class StateForm(forms.ModelForm):
    class Meta:
        model=Statemodel
        fields=['state_name',]

class CityForm(forms.ModelForm):
    class Meta:
        model=Citymodel
        fields="__all__"
        exclude=('City_no',)

class AreaForm(forms.ModelForm):
    class Meta:
        model=Areamodel
        fields="__all__"
        exclude=('Area_no',)

class RestaurantTypeForm(forms.ModelForm):
    class Meta:
        model = RestaurantTypeModel
        fields = ('type_name',)