from django import forms
from s_admin.models import Statemodel,Citymodel,Areamodel,RestautantType

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

class RestaurantForm(forms.ModelForm):
    class Meta:
        model=RestautantType
        fields=['type_name']