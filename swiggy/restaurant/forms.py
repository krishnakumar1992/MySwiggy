from django import forms
from restaurant.models import RestaurantModel,RestaurantProduct

class RestaurantForm(forms.ModelForm):
    restro_password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = RestaurantModel
        fields = "__all__"
        exclude = ('restro_id', 'restro_otp', 'restro_status')

class RestaurantLoginForm(forms.Form):
    contact_no=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your UserName','class':'text_box'}),label="")
    password=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password','class':'text_box'}),label="")

class productForm(forms.ModelForm):
    product_name = forms.CharField(max_length=60,widget=forms.TextInput(attrs={'placeholder': 'Product Name'}))
    product_quantity = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'quty'}))
    product_price = forms.FloatField(widget=forms.TextInput(attrs={'id': 'price','class':'input'}))
    product_discount = forms.FloatField(widget=forms.TextInput(attrs={'id': 'discount','class':'input'}))
    product_status = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'placeholder': 'Enter Status Hare '}))
    product_result = forms.FloatField(widget=forms.TextInput(attrs={'id': 'result','readonly':''}))

    class Meta:
        model=RestaurantProduct
        fields=('product_name','product_quantity','product_price','product_discount','product_result','product_status','Product_img')
        exclude=('product_id','restro_name')
