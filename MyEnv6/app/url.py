from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('students/',views.students,name='students'),
    path('marksheet/', views.student_marksheet, name='marksheet'),
    path('login',views.login_view , name='login'),
    path('register',views.register,name='register'),
    path('thank_you',views.thank_you,name='thank_you')
]