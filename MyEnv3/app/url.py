from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('detail/',views.detail),
    path('about/',views.about),
]