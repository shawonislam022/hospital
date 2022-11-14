from django.db import models

# Create your models here.
class contactus(models.Model):
    name = models.CharField(max_length=50 ,null=True)
    email = models.EmailField(max_length=50,null=True)
    message = models.CharField(max_length=1000,null=True)

class Signup(models.Model):
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)

class Login(models.Model):
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)

class Appointment(models.Model):
    
    pname = models.CharField(max_length=50,null=True)
    dept = models.CharField(max_length=50,null=True)
    doctor = models.CharField(max_length=50,null=True)
    phoneno = models.CharField(max_length=50,null=True)
    problem = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length = 50,null=True)
    gender = models.CharField(max_length= 50,null=True)

class Blood(models.Model):
    pname = models.CharField(max_length=50,null=True)
    pd = models.CharField(max_length=50,null=True)
    ddate= models.DateField(null=True)
    quantity = models.IntegerField(null=True)
    contactno = models.IntegerField(null=True)
    dtime = models.TimeField(null=True)
    dcity = models.CharField(max_length=50 ,null=True)
    dadd = models.CharField(max_length=50,null=True)
    bloodg = models.CharField(max_length = 50,null=True)

class Ambulance(models.Model):
    type = models.CharField(max_length=50,null=True)
    source = models.CharField(max_length=50,null=True)
    to = models.CharField(max_length= 50,null=True)
    dep = models.DateField(null=True)
    nop = models.IntegerField(null=True)
    contactno = models.IntegerField(null=True)
    dtime = models.TimeField(null=True)
    dadd = models.CharField(max_length=50,null=True)
    oxygen = models.CharField(max_length = 50,null=True)
class Blooddonor(models.Model):
    name=models.CharField(max_length=50,null=True)
    bgroup=models.CharField(max_length=50,null=True)
    ldate=models.DateField(null=True)
    quantity=models.IntegerField(null=True)
    contactno=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    city=models.CharField(max_length=50,null=True)
    add=models.CharField(max_length=50,null=True)
    
    

 





