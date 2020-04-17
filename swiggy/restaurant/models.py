from django.db import models
from s_admin.models import Areamodel,RestautantType

# Create your models here.
class RestaurantModel(models.Model):
    rest_id=models.AutoField(primary_key=True)
    rest_name=models.CharField(unique=True,max_length=40)
    rest_contact=models.IntegerField(unique=True)
    rest_Email=models.EmailField(max_length=50,unique=True)
    rest_area=models.ForeignKey(Areamodel,on_delete=models.CASCADE)
    rest_type=models.ForeignKey(RestautantType,on_delete=models.CASCADE)
    rest_password=models.CharField(max_length=50)
    rest_otp=models.IntegerField()
    rest_statue=models.CharField(max_length=50,default=False)