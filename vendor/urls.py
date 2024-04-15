"""
URL configuration for vendor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_deatails import views as usjac

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register',usjac.Register,name='Register'),
    path('address', usjac.address01, name='address'),
    path('contact_deatails',usjac.contactdeatails,name='contact_deatails'),
    path('vendor',usjac.vendordeatails,name='vendor'),

    path('getregister',usjac.Getregister,name='getregister'),
    path('getaddress',usjac.getaddress,name='getaddress'),
    path('getvendor', usjac.getvendor, name='getvendor'),

    path('Getmodel/<pk>',usjac.getmodel,name='Getmodel'),
    path('GetAddress/<pk>',usjac.getaddress001,name='GetAddress'),
    path('GetContact/<pk>', usjac.getcontact001, name='GetContact'),
    path('GetVendor/<pk>', usjac.getvendor001, name='GetVendor'),

    path('DeleteRegister/<pk>',usjac.delete_register,name='DeleteRegister'),
    path('DeleteAddress/<pk>', usjac.delete_address, name='DeleteAddress'),
    path('DeleteContact/<pk>', usjac.delete_contact, name='DeleteContact'),
    path('DeleteVendor/<pk>', usjac.delete_vendor, name='DeleteVendor'),

    path('index',usjac.Index,name='index')





]
