from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
# Create your views here.
from .models import Contact,Collagelist,Collagedetail
from .forms import student_form,userform
from django.contrib.auth.models import User
from django.http import *
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import  ObjectDoesNotExist
from django.db.models import Q

def home(request):

    collage_ob = Collagelist.objects.all()
    return render(request, "collage/them1.html",{})

def index(request):
    list_use = Collagelist.Objects.all()
    return render(request,"collage/indexuse.html",{"list_use":list_use})


def detail (request):
    ob = Collagelist.objects.all().order_by("name")
    return render(request, "collage/index_detail.html",{'ob': ob})

def student1(request):
    ob1 = Collagelist.objects.all().order_by("name")

    if request.method == "POST":
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student1/')

    else:
        form = student_form()
        return render(request, 'collage/student.html',{'form':form, 'std' : ob1})



def registration(request):
    if request.method == 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username = username,first_name= first_name, last_name = last_name, email = email, password = password)
            messages.success(request,"user registration successfully")
            usr = auth.authenticate(username=username, password=password)
            auth.login(request,usr)
            return render(request,"collage/welcome.html")

    else:
        form1 = userform()
    return render(request,'collage/registration.html',{'frm': form1})

"""--------------------------------------------------------------------------------------------------------------"""

def login(request):
    if request.method =="POST":
        username = request.POST['user']
        password = request.POST['pas']

        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return render(request,"collage/welcome.html")

            else:
                messages.error(request, "  you are not a user ")

        except auth.ObjectDoesNotExist :

            print("invalid user")

    return render(request,"collage/login.html")

def logout(request):
    auth.logout(request)
    return render(request,"collage/login.html")

"""--------------------------------------------------------------------------------------------------------------"""



def search(request):
    if request.method == "POST":
        srch = request.POST['srh']

        if srch:
            match = student1.objects.filter(Q(name_icontains = srch)
                                                 )

            if match:
                return render(request,"collage/search.html",{'sr': match})
            else:
                messages.error(request,"no result found")
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'collage/search.html',{})



def result(request,id):
    pass

def vote(request,id):
    pass
