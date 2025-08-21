from django.shortcuts import render

def home(req):
    return render(req,'Home.html')
def about(req):
    return render(req,'about.html')
def login(req):
    return render(req,'login.html')
def detail(req):
    return render(req,'detail.html')
