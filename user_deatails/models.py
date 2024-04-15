from django.db import models
from  django.utils.timezone import now

# Create your models here.

class Registermodel(models.Model):

    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mblenum=models.BigIntegerField()
    email=models.EmailField(max_length=400,null=True)

class address(models.Model):
    line1=models.CharField(max_length=100)
    line2=models.CharField(max_length=100)
    pincode=models.BigIntegerField()
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class contact_deatails(models.Model):
    mobilenum=models.BigIntegerField()
    emailid=models.EmailField(max_length=200,null=True)
    accno=models.BigIntegerField()
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by=models.IntegerField(null=True,blank=True)
    updated_date=models.DateTimeField(null=True,blank=True)



class vendor(models.Model):
    vendor_name=models.CharField(max_length=200)
    vendor_code=models.CharField(max_length=100)
    vendor_gst=models.CharField(max_length=200)
    vendor_branch=models.CharField(max_length=200)
    vendor_pan=models.CharField(max_length=100)
    address=models.ForeignKey(address,on_delete=models.SET_NULL,null=True)
    contact_deatails=models.ForeignKey(contact_deatails,on_delete=models.SET_NULL,null=True)
    status=models.SmallIntegerField(default=1)
    created_by=models.IntegerField(null=False,blank=False)
    created_date=models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)






