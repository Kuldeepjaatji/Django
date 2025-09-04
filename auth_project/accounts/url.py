# from django.urls import path
# from . import views

# urlpatterns = [
#     
#     path('register', views.register),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service', views.service, name='service'),
    path('login', views.login, name='login'),
    path('Contect', views.Contect, name='Contect'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
