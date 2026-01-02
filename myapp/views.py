import datetime
import json

import ob as ob
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from myapp.models import *

def logout(request):
    auth.logout(request)
    return render(request,"index.html")

# Create your views here.
def login(request):
    return render(request, 'index.html')
def login_post(request):
        username=request.POST['textfield']
        password=request.POST['textfield2']
        try:
            ob=logintable.objects.get(username=username,password=password)
            request.session['lid']=ob.id
            if ob.type == 'admin':
                    ob1=auth.authenticate(username='admin',password='admin')
                    if ob1 is not None:
                        auth.login(request,ob1)
                    return HttpResponse('''<script>alert("admin logined successfully");window.location='/adminhome'</script>''')
            elif ob.type== 'ashaworker':
                ob1 = auth.authenticate(username='admin', password='admin')
                if ob1 is not None:
                    auth.login(request,ob1)
                return HttpResponse('''<script>alert("ashaworker logined successfully");window.location='/ashaworker_home'</script>''')
            elif ob.type == 'expert':
                ob1 = auth.authenticate(username='admin', password='admin')
                if ob1 is not None:
                    auth.login(request,ob1)
                return HttpResponse('''<script>alert("expert logined successfully");window.location='/expert_home'</script>''')
            else:
                return HttpResponse('''<script>alert("invalid");window.location='/'</script>''')
        except Exception as e:
            print(f"An error occurred: {e}")
            return HttpResponse('''<script>alert("something went wrong");window.location='/'</script>''')

@login_required(login_url='/')
def addashaworker(request):
    ob=ward.objects.all()
    ob1=panchayath.objects.all()
    return render(request,'admin/add ashaworker.html',{'data':ob,'data1':ob1})

@login_required(login_url='/')
def addashaworker_post(request):
    name=request.POST['textfield2']
    ward=request.POST['select']
    phone=request.POST['textfield4']
    email=request.POST['textfield5']
    regno=request.POST['textfield6']
    panchayath=request.POST['select1']
    username=request.POST['textfield7']
    password=request.POST['textfield8']
    image=request.FILES['file']

    fs=FileSystemStorage()
    date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
    fs.save(date,image)
    path=fs.url(date)
    # fp=fs.save(image.name,image)

    ob=logintable()
    ob.username=username
    ob.password=password
    ob.type='ashaworker'
    ob.save()

    ob1=ashaworker()
    ob1.image = path
    ob1.LOGIN = ob
    ob1.name=name
    ob1.WARD_id=ward
    ob1.phone=phone
    ob1.email=email
    ob1.regno=regno
    ob1.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/ashaworkermanagement'</script>''')

@login_required(login_url='/')
def addpanchayath(request):
    return render(request,'admin/add panchayath.html')

@login_required(login_url='/')
def addpanchayath_post(request):
    place=request.POST['textfield']
    post=request.POST['textfield2']
    pin=request.POST['textfield3']
    email=request.POST['textfield4']
    phone=request.POST['textfield5']
    ob=panchayath()
    ob.place=place
    ob.pin=pin
    ob.post=post
    ob.contact=phone
    ob.email=email
    ob.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/managepanchayath'</script>''')


@login_required(login_url='/')
def adminhome(request):
    return render(request,'admin/index.html')

@login_required(login_url='/')
def ashaworkermanagement(request):
    ob=ashaworker.objects.all()
    return render(request,'admin/ashaworkermanagement.html',{'data':ob})

@login_required(login_url='/')
def manageexpert(request):
    return render(request, 'admin/add expert.html')
@login_required(login_url='/')
def addexpert_post(request):
    image = request.FILES['textfield6']
    name=request.POST['textfield']
    place=request.POST['textfield2']
    pin=request.POST['textfield3']
    post=request.POST['textfield4']
    contact=request.POST['textfield9']
    email=request.POST['textfield10']
    gender=request.POST['select']
    username = request.POST['textfield7']
    password = request.POST['textfield8']
    fs = FileSystemStorage()
    fp = fs.save(image.name, image)

    ob = logintable()
    ob.username = username
    ob.password = password
    ob.type = 'expert'
    ob.save()

    ob1 = expert()
    ob1.image= fp
    ob1.LOGIN = ob
    ob1.name=name
    ob1.place=place
    ob1.pin=pin
    ob1.post=post
    ob1.contact=contact
    ob1.email=email
    ob1.gender=gender
    ob1.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/viewexpert'</script>''')

@login_required(login_url='/')
def managepanchayath(request):
    ob=panchayath.objects.all()
    return render(request,'admin/manage pnchyth.html',{'data':ob})
@login_required(login_url='/')
def viewashaworker(request):
    return render(request,'admin/view ashaworker.html')
@login_required(login_url='/')
def viewexpert(request):
    ob=expert.objects.all()


    return render(request, 'admin/view expert.html',{'data':ob})
@login_required(login_url='/')
def  wardmanagement(request):
    ob=ward.objects.all()
    return render(request,'admin/ward management.html',{'data':ob})
@login_required(login_url='/')
def addwardmanagement(request):
    ob=panchayath.objects.all()

    return render(request,'admin/add wardmnagement.html',{'data':ob})
@login_required(login_url='/')
def addward_post(request):
    panchayath=request.POST['pl']
    wardnumber=request.POST['textfield']
    ob=ward()
    ob.PANCHAYATH_id=panchayath
    ob.wardnumder=wardnumber
    ob.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/addwardmanagement'</script>''')

@login_required(login_url='/')
def deletepanchayath(request,id):
    ob=panchayath.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/managepanchayath'</script>''')
@login_required(login_url='/')
def deleteexpert(request,id):
    ob=expert.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/viewexpert'</script>''')
@login_required(login_url='/')
def deleteward(request,id):
    ob=ward.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/wardmanagement'</script>''')
@login_required(login_url='/')
def deleteashaworker(request,id):
    ob=ashaworker.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/viewashaworker'</script>''')
@login_required(login_url='/')
def editpanchayth(request,id):
    request.session['pid']=id
    ob=panchayath.objects.get(id=id)
    return render(request,'admin/edit panchayth.html',{'data':ob})
@login_required(login_url='/')
def editpanchayathpost(request):
    ob=panchayath.objects.get(id=request.session['pid'])
    ob.place=request.POST['textfield']
    ob.pin=request.POST['textfield3']
    ob.post=request.POST['textfield2']
    ob.contact=request.POST['textfield5']
    ob.email=request.POST['textfield4']
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/managepanchayath'</script>''')
@login_required(login_url='/')
def editward(request,id):
    request.session['wid']=id
    a=panchayath.objects.all()
    ob=ward.objects.get(id=id)
    return render(request,'admin/editward.html',{'data': ob,'data1':a})
@login_required(login_url='/')
def editwardpost(request):
    ob = ward.objects.get(id=request.session['wid'])
    ob.PANCHAYATH_id = request.POST['pl']
    ob.wardnumder= request.POST['textfield']
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/wardmanagement'</script>''')
@login_required(login_url='/')
def editashaworker(request,id):
    request.session['wid']=id
    a=panchayath.objects.all()
    ob=ward.objects.all()
    aa=ashaworker.objects.get(id=id)
    return render(request,'admin/editashawork.html',{'data': ob,'data1':a,'asha':aa})
@login_required(login_url='/')
def editashaworkpost(request):
    name=request.POST['textfield2']
    ward=request.POST['select']
    phone=request.POST['select']
    email=request.POST['textfield5']
    regno=request.POST['textfield6']
    ob=ashaworker.objects.get(id=request.session['wid'])
    if 'file' in request.FILES:
        image = request.FILES['file']

        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)

        ob.image = path
    ob.name = name
    ob.ward=ward
    ob.phone=phone
    ob.email=email
    ob.regno=regno
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/ashaworkermanagement'</script>''')
@login_required(login_url='/')
def editexpert(request,id):
    request.session['eid']=id
    ob=expert.objects.get(id=id)
    return render(request,'admin/editexpert.html',{'data': ob})
@login_required(login_url='/')
def editexpertpost(request):
    ob = expert.objects.get(id=request.session['eid'])
    name = request.POST['textfield']
    place= request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    contact = request.POST['textfield9']
    email = request.POST['textfield10']
    gender = request.POST['select']

    if 'file' in request.FILES:
        image=request.FILES['file']
        fs=FileSystemStorage()
        fp=fs.save(image.name,image)
        ob.image=fp
    ob.name=name
    ob.place=place
    ob.pin=pin
    ob.post=post
    ob.contact=contact
    ob.email=email
    ob.gender=gender

    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/viewexpert'</script>''')


# ashaworker
@login_required(login_url='/')
def add_allocated_food(request):
    ob=food.objects.all()
    return render(request, 'ashaworker/add allocated food.html',{'data':ob})
@login_required(login_url='/')
def add_allocated_food_post(request):
    food=request.POST['select']
    day=request.POST['month']
    ob=foodallocation()
    ob.FOOD_id=food
    ob.day=day
    ob.date=datetime.datetime.now()
    ob.parent=mother.objects.get(id=request.session['aid'])
    ob.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/verify_mothers'</script>''')

@login_required(login_url='/')
def add_food(request):
    return render(request, 'ashaworker/add food.html')
@login_required(login_url='/')
def add_food_post(request):
    category=request.POST['textfield']
    foodname=request.POST['textfield2']
    quantity=request.POST['textfield3']
    ob=food()
    ob.foodname=foodname
    ob.category=category
    ob.quantity=quantity
    ob.ashaworkerid=ashaworker.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/view_food'</script>''')



@login_required(login_url='/')
def view_food(request):
    ob=food.objects.filter(ashaworkerid__LOGIN_id=request.session['lid'])
    return render(request, 'ashaworker/view food.html',{'data':ob})
@login_required(login_url='/')
def addchild(request):
    return render(request,'ashaworker/add child.html')
@login_required(login_url='/')
def addchildpost(request):
    name=request.POST['textfield']
    weight=request.POST['textfield2']
    age=request.POST['textfield3']
    ob=child()
    ob.name=name
    ob.weight=weight
    ob.age=age
    ob.PARENT=mother.objects.get(id=request.session['cid'])
    ob.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/verify_mothers'</script>''')



@login_required(login_url='/')
def addvacc_details_of_child(request):
    ob=vaccination.objects.all()
    return render(request,'ashaworker/add vacc details of child.html',{'data':ob})
@login_required(login_url='/')
def add_vacc_detail_child_post(request):
    vaccine=request.POST['select']
    date=request.POST['textfield3']
    ob=childvaccinationdetails()
    ob.CHILDID=child.objects.get(id=request.session['vid'])
    ob.date=date
    ob.VACCINATIONID_id=vaccine
    ob.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/verify_mothers'</script>''')
@login_required(login_url='/')
def add_vacc_details(request):
    return render(request,'ashaworker/add vaccination details.html')
@login_required(login_url='/')
def add_vacc_detail_post(request):
    name=request.POST['textfield']
    date=request.POST['textfield3']
    desc=request.POST['textfield4']
    place = request.POST['textfield2']


    ob=vaccination()
    ob.ashaworkerid=ashaworker.objects.get(LOGIN_id=request.session['lid'])
    ob.name=name
    ob.date=date
    ob.desc=desc
    ob.place=place
    ob.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/view_vacc_details'</script>''')
@login_required(login_url='/')
def ashaworker_home(request):
    return render(request,'ashaworker/ashaworkerindex.html')
@login_required(login_url='/')
def verify_mothers(request):
    b=ashaworker.objects.get(LOGIN_id=request.session['lid'])
    a=mother.objects.filter(WARD_id=b.WARD.id)
    return render(request,'ashaworker/verify mothers.html',{'data':a})
@login_required(login_url='/')
def accept_mother(request,id):
    request.session['mid']=id
    ob=logintable.objects.get(id=id)
    ob.type='user'
    ob.save()
    return HttpResponse('''<script>alert("accept successfully");window.location='/verify_mothers'</script>''')

@login_required(login_url='/')
def reject_mother(request,id):
    request.session['mid']=id
    ob=logintable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("reject successfully");window.location='/verify_mothers'</script>''')


@login_required(login_url='/')
def view_allocated_food(request,id):
    request.session['aid']=id
    ob=foodallocation.objects.filter(parent_id=id)
    return render(request, 'ashaworker/view alloacted food.html',{'data':ob})

@login_required(login_url='/')
def view_child(request,id):
    request.session['cid']=id
    ob=child.objects.filter(PARENT_id=id)
    return render(request,'ashaworker/view child.html',{'data':ob})
@login_required(login_url='/')
def view_vacc_details(request):
    ob=vaccination.objects.filter(ashaworkerid__LOGIN_id=request.session['lid'])
    return render(request,'ashaworker/view vacc details.html',{'data':ob})

@login_required(login_url='/')
def edit_vaccination(request,id):
    request.session['eid']=id
    ob=vaccination.objects.get(id=id)
    return render(request,'ashaworker/editvaccdetails.html',{'data':ob})

@login_required(login_url='/')
def edit_vaccination_post(request):
    ob = vaccination.objects.get(id=request.session['eid'])
    ob.name = request.POST['textfield']
    ob.date = request.POST['textfield3']
    ob.desc = request.POST['textfield4']
    ob.place=request.POST['textfield2']
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/view_vacc_details'</script>''')

@login_required(login_url='/')
def view_vacc_details_child(request,id):
    request.session['vid']=id
    ob = childvaccinationdetails.objects.filter(CHILDID_id=id)
    return render(request,'ashaworker/view vacc details of child.html',{'data':ob})


@login_required(login_url='/')
def deleteechild(request,id):
    ob=child.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/verify_mothers'</script>''')

@login_required(login_url='/')
def editvacc_detail_of_child(request,id):
    request.session['cid']=id
    ob=vaccination.objects.all()
    a=childvaccinationdetails.objects.get(id=id)
    return render(request,'ashaworker/editchild vacc details.html',{'data1':a,'data':ob})

@login_required(login_url='/')
def editvacc_detail_of_child_post(request):
    vacc=request.POST['select']
    date=request.POST['textfield3']
    ob=childvaccinationdetails.objects.get(id=request.session['cid'])
    ob.VACCINATIONID_id=vacc
    ob.date=date
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/verify_mothers'</script>''')

@login_required(login_url='/')
def deletevacc_details_child(request,id):
    ob=childvaccinationdetails.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/verify_mothers'</script>''')
@login_required(login_url='/')
def delete_vacc_details(request,id):
    ob=vaccination.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/view_vacc_details'</script>''')
@login_required(login_url='/')
def delete_food(request,id):
    ob=food.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/view_food'</script>''')

@login_required(login_url='/')
def delete_foodallocation(request,id):
    ob=foodallocation.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/verify_mothers'</script>''')
@login_required(login_url='/')
def edit_food_allocation(request,id):
    request.session['fid']=id
    ob=food.objects.all()
    return render(request,'ashaworker/editfood allocation.html',{'data':ob})
@login_required(login_url='/')
def edit_food_allocation_post(request):
    ob=foodallocation.objects.get(id=request.session['fid'])
    ob.FOOD_id=request.POST['select']
    ob.day=request.POST['month']
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/verify_mothers'</script>''')

@login_required(login_url='/')
def edit_food(request,id):
    request.session['fid'] = id
    ob = food.objects.get(id=id)
    return render(request, 'ashaworker/editfood.html', {'data': ob})

@login_required(login_url='/')
def edit_food_post(request):
    ob = food.objects.get(id=request.session['fid'])
    ob.category = request.POST['textfield']
    ob.foodname = request.POST['textfield2']
    ob.quantity=request.POST['textfield3']
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/view_food'</script>''')

#expert
@login_required(login_url='/')
def expert_home(request):
    return render(request, 'expert/expertindex.html')

@login_required(login_url='/')
def add_shedule(request):
    return render(request, 'expert/add shedule.html')
@login_required(login_url='/')
def add_shedule_post(request):
    date=request.POST['textfield3']
    from_time=request.POST['textfield2']
    to_time=request.POST['textfield4']
    ob=shedule()
    ob.date=date
    ob.from_time=from_time
    ob.to_time=to_time
    ob.EXPERT=expert.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/view_shedule'</script>''')


@login_required(login_url='/')
def view_shedule(request):
    ob=shedule.objects.filter(EXPERT__LOGIN_id=request.session['lid'])
    return render(request, 'expert/view shedule.html',{'data':ob})

@login_required(login_url='/')
def deletee_shedule(request,id):
    ob=child.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete successfully");window.location='/view_shedule'</script>''')
@login_required(login_url='/')
def edit_shedule(request,id):
    request.session['sid'] = id
    ob = shedule.objects.get(id=request.session['sid'])
    return render(request, 'expert/edit shedule.html', {'data': ob})
@login_required(login_url='/')
def edit_shedule_post(request):
    ob = shedule.objects.get(id=request.session['sid'])
    ob.date = request.POST['textfield3']
    ob.from_time = request.POST['textfield4']
    ob.to_time = request.POST['textfield5']
    ob.EXPERT = expert.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("update successfully");window.location='/view_shedule'</script>''')
@login_required(login_url='/')
def accept_shedule(request,id):
    request.session['sid']=id
    ob=booking.objects.get(id=id)
    ob.status='accept'
    ob.save()
    return HttpResponse('''<script>alert("accept successfully");window.location='/view_booking'</script>''')

@login_required(login_url='/')
def reject_shedule(request,id):
    request.session['sid']=id
    ob=booking.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("reject successfully");window.location='/view_booking'</script>''')


@login_required(login_url='/')
def view_booking(request):
    ob=booking.objects.filter(SHEDULE__EXPERT__LOGIN_id=request.session['lid'])
    return render(request, 'expert/view booking.html',{'val':ob})


@login_required(login_url='/')
def add_prescription(request,id):
    request.session['bid']=id
    ob=booking.objects.get(id=id)
    return render(request, 'expert/add_prescription.html',{'val':ob})

def add_prescription_post(request):
    file=request.FILES['file']
    fs=FileSystemStorage()
    fp=fs.save(file.name,file)
    ob=prescription()
    ob.file=fp
    ob.BOOKING=booking.objects.get(id=request.session['bid'])
    ob.save()
    return HttpResponse('''<script>alert("added successfully");window.location='/view_booking'</script>''')



@login_required(login_url='/')
def view_profile(request):
    ob=expert.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'expert/view profile.html',{'val':ob})





#############android######################



def logincode(request):
    print(request.POST)
    un = request.POST['username']
    pwd = request.POST['password']
    print(un, pwd)
    try:
        ob = logintable.objects.get(username=un, password=pwd)

        if ob is None:
            data = {"task": "invalid"}
        else:
            print("in user function")
            data = {"task": "valid", "lid": ob.id,"type":ob.type}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)



def view_motherprofile(request):
    lid=request.POST['lid']
    ob=mother.objects.get(LOGIN_id=lid)
    return JsonResponse({'bid':ob.id,'status':'ok','name':ob.name,'place':ob.place,'pin':str(ob.pin),'post':ob.post,'contact':ob.contact,'email':ob.email,'photo':ob.image.url})



def userreg(request):
    name=request.POST['name']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    contact=request.POST['contact']
    email=request.POST['email']
    ward=request.POST['ward']
    image=request.FILES['image']
    username=request.POST['username']
    password=request.POST['password']


    fs=FileSystemStorage()
    fp=fs.save(image.name,image)


    obb=logintable()
    obb.username=username
    obb.password=password
    obb.type='user'
    obb.save()
    ob=mother()
    ob.name=name
    ob.place=place
    ob.pin=pin
    ob.post=post
    ob.contact=contact
    ob.email=email
    ob.image=fp
    ob.WARD_id=ward
    ob.LOGIN=obb
    ob.save()
    return JsonResponse({'status':'OK'})




def view_expert(request):
    ob=expert.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'name':i.name,'place':i.place,'pin':i.pin,'post':i.post,'contact':i.contact,'email':i.email,'image': request.build_absolute_uri(i.image.url),'gender':i.gender,'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def motherview_shedule(request):
    lid=request.POST['lid']
    expert_id=request.POST['expert_id']
    ob=shedule.objects.filter(EXPERT_id=expert_id)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'date':i.date,'from_time':i.from_time,'to_time':i.to_time,'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def view_feedingremainder(request):
    lid=request.POST['lid']
    ob=reminder.objects.filter(PARENT__LOGIN_id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'time':i.time,'desc':i.desc,'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})

def add_feedingremainder(request):
    desc = request.POST['desc']
    time = request.POST['time']

    lid = request.POST['lid']
    lob = reminder()
    lob.PARENT = mother.objects.get(LOGIN_id=lid)
    lob.desc = desc
    lob.time = time
    lob.save()
    return JsonResponse({'task': 'ok'})

# def booknow(request):
#     shedule = request.POST['shedule_id']
#     lid = request.POST['lid']
#     lob = booking()
#     lob.PARENT = mother.objects.get(LOGIN_id=lid)
#     lob.SHEDULE = shedule
#     lob.date = datetime.datetime.now()
#     lob.status='pending'
#     lob.save()
#     return JsonResponse({'task': 'ok'})

def booknow(request):
    try:
        shedule_id = request.POST['shedule_id']
        lid = request.POST['lid']

        # Fetch the mother instance using lid
        parent_instance = mother.objects.get(LOGIN_id=lid)

        # Fetch the shedule instance using shedule_id
        try:
            shedule_instance = shedule.objects.get(id=shedule_id)
        except shedule.DoesNotExist:
            return JsonResponse({'task': 'error', 'message': 'Invalid schedule ID'})

        # Create and save the booking
        lob = booking()
        lob.PARENT = parent_instance
        lob.SHEDULE = shedule_instance  # Assign the actual instance
        lob.date = datetime.datetime.now()
        lob.status = 'pending'
        lob.save()

        return JsonResponse({'task': 'ok'})

    except Exception as e:
        return JsonResponse({'task': 'error', 'message': str(e)})


def user_view_booking(request):
    lid=request.POST['lid']
    ob = booking.objects.filter(PARENT__LOGIN_id=lid)
    print(ob, "HHHHHHHHHHHHHHH")
    mdata = []
    for i in ob:
        data = {'date': i.date, 'stattus': i.status,'from_time':i.SHEDULE.from_time,'to_time':i.SHEDULE.to_time,'expert':i.SHEDULE.EXPERT.name,'id': i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status": "ok", "data": mdata})




def user_view_prescription(request):
    lid=request.POST['lid']
    ob = prescription.objects.filter(BOOKING__PARENT__LOGIN_id=lid)
    print(ob, "HHHHHHHHHHHHHHH")
    mdata = []
    for i in ob:
        data = {'DOCTOR': i.BOOKING.SHEDULE.EXPERT.name, 'file': request.build_absolute_uri(i.file.url),'id': i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status": "ok", "data": mdata})

# def view_childd(request):
#     lid = request.POST['lid']
#     bid = request.POST['bid']
#     ob = child.objects.filter(PARENT_id=bid)
#     return JsonResponse({'status': 'ok', 'name': ob.name, 'weight': ob.weight,'age':ob.age})



def view_childd(request):
    if request.method == 'POST':
        bid = request.POST.get('bid')  # Get the mother's ID (bid)
        children = child.objects.filter(PARENT_id=bid)  # Get all children linked to the mother

        if children.exists():
            child_list = [
                {'name': c.name, 'weight': str(c.weight), 'age': str(c.age)}
                for c in children
            ]
            return JsonResponse({'status': 'ok', 'children': child_list})
        else:
            return JsonResponse({'status': 'error', 'message': 'No children found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def add_baby(request):
    name = request.POST['name']
    weight = request.POST['weight']
    age = request.POST['age']
    lid = request.POST['lid']
    lob = child()
    lob.PARENT = mother.objects.get(LOGIN_id=lid)
    lob.name = name
    lob.weight=weight
    lob.age=age
    lob.save()
    return JsonResponse({'task': 'ok'})


import json
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Configure Google Gemini API
GOOGLE_API_KEY = 'AIzaSyB_G0I9odde2-IwZHB1EgHGmBTKaFvSf6Y'  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini Model
model = genai.GenerativeModel('gemini-1.5-flash')

@csrf_exempt  # Allows POST requests without CSRF token (Only for testing, secure in production)
def chatbot_response(request):
    """
    Handles user input and generates a response from the Gemini API.
    """
    if request.method == 'POST':
        try:
            # Parse JSON request body
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()

            if not user_message:
                return JsonResponse({'response': 'Please enter a valid question.'})

            # Generate response from Gemini
            gemini_response = model.generate_content(user_message)

            # Ensure response is always JSON formatted
            return JsonResponse({'response': gemini_response.text.strip()})

        except json.JSONDecodeError:
            return JsonResponse({'response': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            return JsonResponse({'response': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'response': 'Invalid request method. Use POST.'}, status=405)


def user_view_vaccindetails(request):
    lid=request.POST['lid']
    ob = childvaccinationdetails.objects.filter(CHILDID__PARENT__LOGIN_id=lid)
    print(ob, "Fetched vaccination records")

    mdata = []
    for i in ob:
        data = {
            'name': i.VACCINATIONID.name,
            'date': i.date.strftime('%Y-%m-%d') if i.date else '',
            'desc': i.VACCINATIONID.desc,
            'place': i.VACCINATIONID.place,
            'id': i.id
        }
        mdata.append(data)

    print("Returning data:", mdata)
    return JsonResponse({"status": "ok", "data": mdata})




def user_view_ward(request):
    ob = ward.objects.all()
    print(ob, "Fetched vaccination records")

    mdata = []
    for i in ob:
        data = {
            'wno': i.wardnumder,
            'id': i.id
        }
        mdata.append(data)

    print("Returning data:", mdata)
    return JsonResponse({"status": "ok", "data": mdata})