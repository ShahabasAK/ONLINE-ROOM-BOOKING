
from django.db import models

# Create your models here.
class Registration(models.Model):
    reg_id = models.IntegerField()
    first_name =models.CharField(max_length=25)
    last_name =models.CharField(max_length=25)
    email =models.CharField(max_length=25)
    phone =models.TextField(max_length=10)
    password =models.CharField(max_length=25)
    usertype = models.CharField(max_length=25,default='s')

class Login(models.Model):

    username =models.CharField(max_length=25)
    password =models.CharField(max_length=25)



class Payment(models.Model):
    order_id =models.IntegerField()
    amount =models.IntegerField()
    Transaction_id =models.IntegerField()
    Status =models.CharField(max_length=25)

class Addroom(models.Model):
    id=models.IntegerField()
    room_id = models.IntegerField(primary_key='True')
    room_name = models.CharField("room_name", max_length=100)
    room_type = models.CharField("room_type", max_length=20)
    image = models.ImageField("image", upload_to='images/')
    rate = models.CharField("rate", max_length=100)
    discription = models.CharField("discription", max_length=25)
    phone = models.IntegerField()
    location = models.TextField(max_length=100)


