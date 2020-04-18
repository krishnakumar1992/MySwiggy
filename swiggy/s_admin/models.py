from django.db import models

# Create your models here.
class AdminLoginModel(models.Model):
    username=models.CharField(unique=True,max_length=60)
    password=models.CharField(max_length=60)
    otp=models.IntegerField()

class Statemodel(models.Model):
    state_no=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=40,unique=True)
    def __str__(self):
        return self.state_name

class Citymodel(models.Model):
    City_no=models.AutoField(primary_key=True)
    City_name=models.CharField(max_length=40,unique=True)
    State=models.ForeignKey(Statemodel,on_delete=models.CASCADE)
    def __str__(self):
        return self.City_name

class Areamodel(models.Model):
    Area_no=models.AutoField(primary_key=True)
    Area_name=models.CharField(max_length=40,unique=True)
    City=models.ForeignKey(Citymodel,on_delete=models.CASCADE)


class RestaurantTypeModel(models.Model):
    no = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name
