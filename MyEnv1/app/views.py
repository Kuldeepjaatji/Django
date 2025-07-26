from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    context = {
        'name':'Kuldeep',
        'marks':[90,69,79,89,99,59,22,23,12,15,33,34],
        'Loggin': False
    }
    return render(req,'Home.html',{'data':context})



def about(req):
    return render(req,'About.html')
# def login(req):
#     return HttpResponse('This is my login page')
# def links(req):
#     return HttpResponse('This is my links page')
# def library(req):
#     return HttpResponse('This is my library page')
# def docs(req):
#     return HttpResponse('This is my docs page')
# def image(req):
#     return HttpResponse('This is my image page')