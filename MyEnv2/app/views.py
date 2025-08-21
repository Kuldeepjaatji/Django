from django.shortcuts import render

def home(req):
    return render(req,'Home.html')

def About(req):
    return render(req,'About.html')

def Loggin(req):
    return render(req,'Loggin.html')

def Server(req):
    return render(req,'Server.html')

def Contact(req):
    return render(req,'Contact.html')
