from django.contrib import admin
from .models import *
#from . import models
# Register your models here.


admin.site.register(contactus)
admin.site.register(Signup)
admin.site.register(Login)
admin.site.register(Appointment)
admin.site.register(Blood)
admin.site.register(Ambulance)
admin.site.register(Blooddonor)



class contactusAdmin(admin.ModelAdmin):
    list_display=['name','email','message']