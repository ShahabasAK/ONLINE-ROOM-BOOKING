import email
from django.shortcuts import render, redirect
from django.db.models import Max
from .models import *
from django.core.files.storage import FileSystemStorage


# from django.http import HttpResponse

# Create your views here.




def adminhome(request):
    return render(request, 'adminhome.html')


def user_home(request):
    return render(request, './resortapp/user_home.html')


def registration(request):
    return render(request, './resortapp/registration.html')


def homepage(request):
    return render(request, './resortapp/homepage.html')


def addrooms(request):
    return render(request, './resortapp/addrooms.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Registration.objects.filter(email=email,password=password,usertype="A"):
            a=Registration.objects.get(email=email,password=password,usertype="A")
            print(type(a))
            request.session["uid"] = a.reg_id
            print(request.session["uid"])

            return render(request, "./resortapp/adminhome.html")
        elif Registration.objects.filter(email=email, password=password, usertype="user"):
            return render(request, "./resortapp/user_home.html")
        else:
            return render(request, "./resortapp/invalid.html")
    else:
        return render(request, "./resortapp/login.html")


# LOGOUT
def addrooms(request):
    if request.method == 'POST':
        a=request.session['uid']

        u_file = request.FILES['image']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)

        p = request.POST.get('room_type')
        d = request.POST.get('room_name')
        pr = request.POST.get('rate')
        q = request.POST.get('discription')
        z = request.POST.get('phone')
        w = request.POST.get('location')

        pd = Addroom(room_type=p, room_name=d, rate=pr, discription=q, image=path, phone=z, location=w, id=a)
        pd.save()

        context = {'msg': 'room added'}
        return render(request, './resortapp/addrooms.html', context)

    else:
        return render(request, './resortapp/addrooms.html')


def logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return login(request)
    else:
        return login(request)


# def registration(request):
# return render(request,'./products/registration.html')


def registration(request):
    if request.method == "POST":
        a = request.POST.get('fname')
        b = request.POST.get('lname')
        c = request.POST.get('email')
        d = request.POST.get('phone')
        e = request.POST.get('password')
        f = request.POST.get('usertype')

        un = c
        pwd = e
        ul = Login(username=un, password=pwd)
        ul.save()
        user_id = Login.objects.all().aggregate(Max('id'))['id__max']


        ab = Registration(reg_id=user_id, first_name=a, last_name=b, email=c, phone=d, password=e,usertype=f)
        ab.save()

        msg = {'msg': 'User Registered'}
        return render(request, "./resortapp/login.html", msg)
    else:
        return render(request, "./resortapp/registration.html")


def profile(request):
    single = Registration.objects.filter(id=request.session['user_id'])
    context = {'details': single}
    return render(request, './resortapp/profile.html', context)


def updateprofile(request):
    if request.method == 'POST':
        user_id = request.session['uid']
        up = Registration.objects.get(id=request.session['uid'])

        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('contact')

        up.first_name = first_name
        up.last_name = last_name
        up.email = email
        up.phone = phone

        up.save()

        context = {'msg': 'User Details Updated', 'up': up}
        return render(request, './resortapp/updateprofile.html', context)

    else:
        user_id = request.session['uid']
        up = Registration.objects.get(id=request.session['uid'])
        context = {'up': up}
        return render(request, './resortapp/updateprofile.html', context)

def viewroom(request):
    a=request.session["uid"]
    viewroom = Addroom.objects.filter(id=a)
    vp = {'details': viewroom}
    return render(request, './resortapp/viewroom.html' ,vp)

def updateroom(request,pk):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        room_type = request.POST.get('room_type')
        rate = request.POST.get('rate')
        discription = request.POST.get('discription')
        phone = request.POST.get('phone')
        up = Addroom.objects.get(room_id=pk)
        up.room_name = room_name

        up.rate = rate
        up.discription = discription
        up.phone=phone
        up.save()
        msg = 'room updated'
        up_l = Addroom.objects.all()
        context = {'details': up_l, 'msg': msg}
        return render(request, './resortapp/viewroom.html', context)
    else:

        up = Addroom.objects.get(room_id=pk)
        context={'up':up}
        return render(request, './resortapp/updateroom.html',context)

def deleteroom(request,room_id):
    a = Addroom.objects.get(room_id=room_id)
    a.delete()
    return redirect('http://127.0.0.1:8000/viewroom')

def about(request):
    return render(request, './resortapp/about.html')

def userroom(request):
    viewroom = Addroom.objects.all()
    vp = {'details': viewroom}
    return render(request, './resortapp/rooms.html',vp)

