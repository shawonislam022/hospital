from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('my_info.urls')),
] 
admin.site.site_header="ICE Medical Database There !"