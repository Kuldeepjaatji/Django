from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('login/',views.login),
    path('links/',views.links),
    path('library/',views.library),
    path('docs/',views.docs),
    path('image/',views.image),
]