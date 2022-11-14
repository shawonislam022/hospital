from django.shortcuts import render
from django.http import HttpResponse
from . import models 
from django.shortcuts import redirect
from .models import *

'''
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        contact.name=name
        contact.email=email
        contact.comments = comments
        contact.save()
        return HttpResponse('<h1>Thanks for Contract with us</h1>')
    return render(request, 'contact.html')'''
# Create your views here.
def index(request):
    if request.method == 'POST':
        login = Login()
        username = request.POST.get('username')
        password = request.POST.get('password')
        login.username=username
        login.password=password
        login.save()
        #return HttpResponse('<h1>Thanks for Contract with us</h1>')
        return redirect('loggedin')
    return render(request,'index.html')
    
def ambulance(request):
    '''class Ambulance(models.Model):
    type = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    to = models.CharField(max_length= 50)
    dep = models.DateField(null=False)
    nop = models.IntegerField()
    contactno = models.IntegerField()
    dtime = models.TimeField(null=False)
    dadd = models.CharField(max_length=50)
    oxygen = models.CharField(max_length = 50)'''
    if request.method == 'POST':
        ambulance = Ambulance()
        type = request.POST.get('type')
        source = request.POST.get('source')
        to = request.POST.get('to')
        dep = request.POST.get('dep')
        nop = request.POST.get('nop')
        contactno = request.POST.get('contactno')
        dtime = request.POST.get('dtime')
        dadd = request.POST.get('dadd')
        oxygen = request.POST.get('oxygen')
        ambulance.type=type
        ambulance.source=source
        ambulance.to=to
        ambulance.dep=dep
        ambulance.nop=nop
        ambulance.contactno=contactno
        ambulance.dtime=dtime
        ambulance.dadd=dadd
        ambulance.oxygen=oxygen
        ambulance.save()
        #return HttpResponse('<h1>Thanks for Contract with us</h1>')
        return redirect('submitpopup')

    return render(request,'ambulance.html')
def appointment(request):
    '''class Appointment(models.Model):
    pname = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=50)
    problem = models.CharField(max_length=200)
    email = models.CharField(max_length = 50)
    gender = models.CharField(max_length= 50)'''
    if request.method == 'POST':
        appointment = Appointment()
        pname = request.POST.get('pname')
        dept = request.POST.get('dept')
        doctor = request.POST.get('doctor')
        phoneno = request.POST.get('phoneno')
        problem = request.POST.get('problem')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        appointment.pname=pname
        appointment.dept=dept
        appointment.doctor=doctor
        appointment.phoneno=phoneno
        appointment.problem=problem
        appointment.email=email
        appointment.gender=gender
        appointment.save()
        #return HttpResponse('<h1>Thanks for Contract with us</h1>')
        return redirect('submitpopup')
    return render(request,'appointment.html')
def blood(request):
    '''class Blood(models.Model):
    pname = models.CharField(max_length=50)
    pd = models.CharField(max_length=50)
    ddate= models.DateField(null=False)
    quantity = models.IntegerField()
    contactno = models.IntegerField()
    dtime = models.TimeField(null = False)
    dcity = models.CharField(max_length=50)
    dadd = models.CharField(max_length=50)
    bloodg = models.CharField(max_length = 50)'''
    if request.method == 'POST':
        blood = Blood()
        pname = request.POST.get('pname')
        pd = request.POST.get('pd')
        ddate = request.POST.get('ddate')
        quantity = request.POST.get('quantity')
        contactno = request.POST.get('contactno')
        dtime = request.POST.get('dtime')
        dcity = request.POST.get('dcity')
        dadd = request.POST.get('dadd')
        bloodg = request.POST.get('bloodg')
        blood.pname=pname
        blood.pd=pd
        blood.ddate=ddate
        blood.quantity=quantity
        blood.contactno=contactno
        blood.dtime=dtime
        blood.dcity=dcity
        blood.dadd=dadd
        blood.bloodg=bloodg
        blood.save()
        
    
        #return HttpResponse('<h1>Thanks for Contract with us</h1>')
        return redirect('submitpopup')
    return render(request,'blood.html')
def blooddonor(request):
    '''class Blooddonor(models.Model):
    name=models.CharField(max_length=50)
    bgroup=models.CharField(max_length=50)
    ldate=models.DateField(null=False)
    quantity=models.IntegerField()
    contactno=models.IntegerField()
    age=models.IntegerField()
    city=models.CharField(max_length=50)
    add=models.CharField(max_length=50)'''
    if request.method == 'POST':
        blooddonor = Blooddonor()
        name = request.POST.get('name')
        bgroup = request.POST.get('bgroup')
        ldate = request.POST.get('ldate')
        quantity = request.POST.get('quantity')
        contactno = request.POST.get('contactno')
        age = request.POST.get('age')
        city = request.POST.get('city')
        add = request.POST.get('add')
        blooddonor.name=name
        blooddonor.bgroup=bgroup
        blooddonor.ldate=ldate
        blooddonor.quantity=quantity
        blooddonor.contactno=contactno
        blooddonor.age=age
        blooddonor.city=city
        blooddonor.add=add
        blooddonor.save()
       

        #return HttpResponse('<h1>Thanks for Contract with us</h1>')
        return redirect('submitpopup')
    return render(request,'blooddonor.html')
def contactus(request):
   
    if request.method == 'POST':
        contact = contactus()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message = message
        contact.save()
        #return HttpResponse('<h1>Thanks for Contract with us</h1>')
        return redirect('submitpopup')
    
    return render(request,'contactus.html')
def joinus(request):
    return render(request,'joinus.html')
def signup(request):
    if request.method == 'POST':
        signup = Signup()
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        signup.username=username
        signup.email=email
        signup.password = password
        signup.save()
        return redirect('submitpopup')
       # return HttpResponse('<h1>Thanks for Contract with us</h1>')
        
      
    return render(request,'signupform.html')
def submitpopup(request):
    return render(request,'submitpopup.html')
def sample(request):
    return render(request,'sample.html')
def home(request):
    return render(request,'home.html')
def signin(request):
    if request.method == 'POST':
        login = Login()
        username = request.POST.get('username')
        password = request.POST.get('password')
        login.username=username
        login.password=password
        login.save()
        '''user = authenticate(request, username=username ,password=password)
if user is not None:
	login(request, user)
	return redirect('home')'''
        #return HttpResponse('<h1>Thanks for Contract with us</h1>')
        return redirect('loggedin')
    return render(request,'signin.html')
def homeafterlogin(request):
    return render(request,'homeafterlogin.html')
def homeafterloginn(request):
    return render(request,'homeafterloginn.html')
def showdata(request):
    login = Login.objects.all()
    for i in login:
        print(login)
    return render(request, 'showdata.html', {'Login': login})
def appointmentdata(request):
    appointment = Appointment.objects.all()
    for i in appointment:
        print(appointment)
    return render(request,'appointmentdata.html', {'Appintment': appointment})

