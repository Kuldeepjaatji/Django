from django import forms
from .models import StudentCorse

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentCorse
        fields = ['name','email','course']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'course' : forms.TextInput(attrs={'class' :'form-control'})
        }