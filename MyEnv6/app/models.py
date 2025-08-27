from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField()
    number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class login(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=5)

    def __str__(self):
        return self.phone

class StudentCorse(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name