from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import  HttpResponse




import json
from user_deatails.models import Registermodel,address,contact_deatails,vendor
@csrf_exempt
@api_view(['POST','GET'])
def Register(request):
    if request.method == "POST":
        b=json.loads(request.body)
        if "id" not in b:
            obj=Registermodel.objects.create(firstname=b['firstname'],lastname=b['lastname'],
                                             userid=b['userid'],password=b['password'],mblenum=b['mblenum'],email=b['email'])
            a=[{'Message':'Data Created'}]
            return HttpResponse(json.dumps(a))
        else:
            obj = Registermodel.objects.filter(id=b['id']).update(firstname=b['firstname'], lastname=b['lastname'],
                                               userid=b['userid'], password=b['password'], mblenum=b['mblenum'],
                                               email=b['email'])
            a = [{'Message': 'Data update'}]
            return HttpResponse(json.dumps(a))

@csrf_exempt
@api_view(['POST','GET'])
def address01(request):
    if request.method =="POST":
        b=json.loads(request.body)
        if "id" not in b:
                obj=address.objects.create(line1=b['line1'],line2=b['line2'],pincode=b['pincode'],state=b['state'],district=b['district'],
                                               city=b['city'],created_by=b['created_by'])

                a = [{'Message': 'Data Created'}]
                return HttpResponse(json.dumps(a))
        else:
                  obj = address.objects.filter(id=b["id"]).update(line1=b['line1'], line2=b['line2'], pincode=b['pincode'], state=b['state'],
                                             district=b['district'], city=b['city'], created_by=b['created_by'])

                  a = [{'Message': 'Data update'}]
                  return HttpResponse(json.dumps(a))



@csrf_exempt
@api_view(['POST','GET'])
def contactdeatails(request):
    if request.method =="POST":
        b=json.loads(request.body)
        if "id" not in b:
            obj=contact_deatails.objects.create(mobilenum=b['mobilenum'],emailid=b['emailid'],accno=b['accno'],created_by=b['created_by'])

            a = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(a))

        else:
            obj = contact_deatails.objects.filter(id=b['id']).update(mobilenum=b['mobilenum'], emailid=b['emailid'], accno=b['accno'],
                                                  created_by=b['created_by'])

            a = [{'Message': 'Data update'}]
            return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['POST','GET'])
def vendordeatails(request):
    if request.method =="POST":
        b=json.loads(request.body)
        if "id" not in b:
                    obj=vendor.objects.create(vendor_name=b['vendor_name'], vendor_code=b['vendor_code'],vendor_gst=b['vendor_gst'],
                    vendor_branch=b['vendor_branch'],vendor_pan=b['vendor_pan'],
                    address_id=b['address'],contact_deatails_id=b['contact_deatails'],created_by=b['created_by'])


                    a = [{'Message': 'Data Created'}]
                    return HttpResponse(json.dumps(a))

        else:

                    obj=vendor.objects.filter(id=b["id"]).update(vendor_name=b['vendor_name'], vendor_code=b['vendor_code'],vendor_gst=b['vendor_gst'],
                    vendor_branch=b['vendor_branch'],vendor_pan=b['vendor_pan'],
                    address_id=b['address'],contact_deatails_id=b['contact_deatails'],created_by=b['created_by'])

                    a = [{'Message': 'Data update'}]
                    return HttpResponse(json.dumps(a))

# get the particular deatails in the table
@csrf_exempt
@api_view(['GET'])
def Getregister(request):
        if request.method == "GET":
         obj=Registermodel.objects.all()
        a=[]
        for i in obj:
            b={"firstname":i.firstname,"lastname":i.lastname}
            a.append(b)

        return HttpResponse(json.dumps(a))

@csrf_exempt
@api_view(['GET'])
def getaddress(request):
        if request.method == "GET":
         obj=address.objects.all()
        a=[]
        for i in obj:
            b={"line1":i.line1,"line2":i.line2,
               "pincode":i.pincode,"state":i.state}
            a.append(b)

        return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def getcontact(request):
        if request.method == "GET":
         obj=contact_deatails.objects.all()
        a=[]
        for i in obj:
            b={"mobilenum":i.mobilenum,"emailid":i.emailid,
               "accno":i.accno}
            a.append(b)

        return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def getvendor(request):
        if request.method == "GET":
         obj=vendor.objects.all()
        a=[]
        for i in obj:
            b={
                "vendor_name":i.vendor_name,
               "vendor_code":i.vendor_code,
               "vendor_gst":i.vendor_gst,
               "vendor_branch":i.vendor_branch,
               "address":{"field1":i.address.line1,"field2":i.address.line2,
               "field3":i.address.pincode},
               "contact_deatails":{"field1":i.contact_deatails.mobilenum,
                "field2":i.contact_deatails.emailid}
            }
            a.append(b)

        return HttpResponse(json.dumps(a))

#get the particular id in the table
@csrf_exempt
@api_view(['GET'])
def getmodel(request,pk):
       a=Registermodel.objects.get(id=pk)
       b={"firstname":a.firstname,"lastname":a.lastname}

       return HttpResponse(json.dumps(b))

@csrf_exempt
@api_view(['GET'])
def getaddress001(request,pk):
       a=address.objects.get(id=pk)
       b={"pincode":a.pincode," state":a. state}

       return HttpResponse(json.dumps(b))


@csrf_exempt
@api_view(['GET'])
def getcontact001(request,pk):
       a=contact_deatails.objects.get(id=pk)
       b={"mobilenum":a.mobilenum," emailid":a. emailid}
       return HttpResponse(json.dumps(b))

@csrf_exempt
@api_view(['GET'])
def getvendor001(request,pk):
       a=vendor.objects.get(id=pk)
       b={"vendor_name":a.vendor_name," vendor_branch":a. vendor_branch}
       return HttpResponse(json.dumps(b))


#delete the id in the table
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def delete_register(request,pk):
      if request.method == "DELETE":
          a=Registermodel.objects.filter(id=pk).delete()
          b=[{'Message': 'Successfully deleted'}]
          return HttpResponse(json.dumps(b))



@csrf_exempt
@api_view(['GET','POST','DELETE'])
def delete_address(request,pk):
      if request.method == "DELETE":
          a=address.objects.filter(id=pk).delete()
          b=[{'Message': 'Successfully deleted'}]
          return HttpResponse(json.dumps(b))


@csrf_exempt
@api_view(['GET','POST','DELETE'])
def delete_contact(request,pk):
      if request.method == "DELETE":
          a=contact_deatails.objects.filter(id=pk).delete()
          b=[{'Message': 'Successfully deleted'}]
          return HttpResponse(json.dumps(b))



@csrf_exempt
@api_view(['GET','POST','DELETE'])
def delete_vendor(request,pk):
      if request.method == "DELETE":
          a=vendor.objects.filter(id=pk).delete()
          b=[{'Message': 'Successfully deleted'}]
          return HttpResponse(json.dumps(b))



@csrf_exempt
@api_view(['GET','POST'])
def Index(request):
    if request.method == "POST":
        pass
    return render(request,'index.html')
















