from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('students/',views.students,name='students'),
    path('marksheet/', views.student_marksheet, name='marksheet')
]