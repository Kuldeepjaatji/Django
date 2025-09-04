from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(req):
    return render(req,'Home.html')
def logout(req):
    return render(req,'logout.html')
# def dashboard(req):
#     return render(req,'dashboard.html')
def about(req):
    return render(req,'About.html')
def service(req):
    return render(req,'Services.html')
def login(req):
    return render(req,'login.html')
def Contect(req):
    return render(req,'Contect.html')


def register(req):
    if req.method =='POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(req,'register.html',{'form':form})


def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(req,username=username,password=password)

        if user:
            login(req,user)
            return redirect('home')
        else:
            return render(req,'login.html',{'error':'invaild credentials'})
        
    return render(req,'login.html')


def logout_view(req):
    logout(req)
    return redirect('login')
    

@login_required(login_url='login')
def dashboard(req):
    return render(req,'dashboard.html')