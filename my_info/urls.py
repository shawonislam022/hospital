from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('ambulance',views.ambulance,name='ambulance'),
    path('appointment',views.appointment,name='appointment'),
    path('blood',views.blood,name='blood'),
    path('blooddonor',views.blooddonor,name='blooddonor'),
    path('contactus',views.contactus,name='contactus'),
    path('joinus',views.joinus,name='joinus'),
    path('signup',views.signup,name='signup'),
    path('submitpopup',views.submitpopup,name='submitpopup'),
    path('sample',views.sample,name='sample'),
    path('home',views.home,name='homei'),
    path('signin',views.signin,name='signin'),
    path('loggedin',views.homeafterlogin,name='loggedin'),
    path('nhome',views.homeafterloginn,name='nhome'),
    path('showdata',views.showdata,name='showdata'),
    path('appointmentdata',views.appointmentdata,name='appointmentdata'),
    path('preloader', views.preloader,name='preloader'),
  
]
