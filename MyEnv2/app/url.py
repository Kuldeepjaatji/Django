from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.About),
    path('loggin/',views.Loggin),
    path('Server/',views.Server),
    path('Contact/',views.Contact)
]
# urlpatterns = [
#     path('',views.About),
#     path('about/',views.About),
#     path('loggin/',views.Loggin),
#     path('Server/',views.Server),
#     path('Contact/',views.Contact)
# ]
# urlpatterns = [
#     path('',views.home),
#     path('about/',views.About),
#     path('loggin/',views.Loggin),
#     path('Server/',views.Server),
#     path('Contact/',views.Contact)
# ]
# urlpatterns = [
#     path('',views.home),
#     path('about/',views.About),
#     path('loggin/',views.Loggin),
#     path('Server/',views.Server),
#     path('Contact/',views.Contact)
# ]
