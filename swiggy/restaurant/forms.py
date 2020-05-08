from django import forms
from restaurant.models import RestaurantModel,RestaurantProduct

class RestaurantForm(forms.ModelForm):
    restro_password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = RestaurantModel
        fields = "__all__"
        exclude = ('restro_id', 'restro_otp', 'restro_status')

class RestaurantLoginForm(forms.Form):
    contact_no=forms.IntegerField()
    password=forms.CharField(max_length=40,widget=forms.PasswordInput)

class productForm(forms.ModelForm):
    class Meta:
        model=RestaurantProduct
        fields=('product_name','product_quantity','product_price','product_discount','product_status','Product_img')
        exclude=('product_id','restro_name')
