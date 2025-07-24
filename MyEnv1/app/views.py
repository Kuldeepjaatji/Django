from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse('Hello Kuldeep Ji')
def about(req):
    return HttpResponse('This is my about page')
def login(req):
    return HttpResponse('This is my login page')
def links(req):
    return HttpResponse('This is my links page')
def library(req):
    return HttpResponse('This is my library page')
def docs(req):
    return HttpResponse('This is my docs page')
def image(req):
    return HttpResponse('This is my image page')