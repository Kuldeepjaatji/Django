from django.shortcuts import render , redirect
from .models import student
from django.db import IntegrityError


def home(req):
    return render(req,'Home.html')
def about(req):
    return render(req,'about.html')
def students(req):
    error = ''
    if req.method =='POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        email = req.POST.get('email')
        number = req.POST.get('number')

        try:

            student.objects.create(name=name , email=email , age=age , number= number)
            return redirect('students')
        except IntegrityError:
            error = 'this is dulicate enter error.'
    return render(req,'students.html')

def student_marksheet(req):
    context = {}
    if req.method == 'POST':
        Hindi = float(req.POST.get('Hindi'))
        English = float(req.POST.get('English'))
        Math = float(req.POST.get('Math'))
        Chemistry = float(req.POST.get('Chemistry'))
        Physic = float(req.POST.get('Physic'))

        total = Hindi + English + Math + Chemistry + Physic

        persent = (total/5)

        parse = persent

        if persent >= 90:
            grade = 'A+'
        elif persent >= 80:
            grade = 'A'
        elif persent >= 70:
            grade = 'B'
        elif persent >= 60:
            grade = 'C'
        else:
            grade = 'D'


        context = {
        'total' : total ,
        'grade' : grade,
        'parse' : parse,
        }
        return render(req,'form.html', context)
    return render(req,'MarkSheet.html')


