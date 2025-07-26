from django.shortcuts import render
# from django.http import HttpResponse


def home(req):
    # return HttpResponse('Hello World')
    return render(req,'Home.html')
def about(req):
    return render(req,'About.html')
    # return HttpResponse('My About page')