from django.shortcuts import render , redirect , get_object_or_404
from .models import student, login , StudentCorse
from django.db import IntegrityError
from .forms import StudentForm


def home(req):
    return render(req,'Home.html')
def about(req):
    return render(req,'about.html')
def thank_you(req):
    return render(req,'thanku.html')
def students(req):
    error = ''
    if req.method =='POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        email = req.POST.get('email')
        number = req.POST.get('number')

        # context = {
        # 'total' : name ,
        # 'grade' : email,
        # 'parse' : age,
        # 'number' : number,
        # }
        # return render(req,'form.html', context)
        try:
            student.objects.create(name=name , email=email , age=age , number= number)
            return redirect('students')
        except IntegrityError:
            error = 'this is dulicate enter error.'
    return render(req,'Students.html')

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

def login_view(req):
    error = ''
    if req.method == 'POST':
        phone = req.POST.get('phone')
        email = req.POST.get('email')
        password = req.POST.get('password')
        
        context = {
        'total' : phone ,
        'grade' : email,
        'parse' : password,
        }
        return render(req,'form.html', context)
    #     try:
    #         login.objects.create(phone=phone , email=email , password=password)
    #         return redirect('login')
    #     except IntegrityError:
    #         error = 'this is dulicate enter error.'
    return render(req,'login.html')


def register(req):
    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = StudentForm()
    return render(req,'register.html',{'form' : form})

def studentAdd(req):
    if req.method == 'POST':
        form = StudentForm(req.POST or None)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(req,'studentAdd.html',{'form' : form})



def student_list(req):
    students = StudentCorse.objects.all()
    return render(req,'student_list.html',{'students':students})



def update_student(req,pk):
    student = get_object_or_404(StudentCorse,pk=pk)
    form = StudentForm(req.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(req,'studentAdd.html',{'form':form})
def delete_student(req,pk):
    student = get_object_or_404(StudentCorse,pk=pk)
    student.delete()
    students = StudentCorse.objects.all()
    return render(req, 'student_list.html', {'students': students})