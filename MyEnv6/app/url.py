from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('students/',views.students,name='students'),
    path('marksheet/', views.student_marksheet, name='marksheet'),
    path('login',views.login_view , name='login'),
    path('register',views.register,name='register'),
    path('thank_you',views.thank_you,name='thank_you'),
    path('student_list',views.student_list,name='student_list'),
    path('studentAdd',views.studentAdd,name='studentAdd'),
    path('update_student/<int:pk>',views.update_student,name='update_student'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student')
]