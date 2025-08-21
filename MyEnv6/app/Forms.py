from django import forms

class MarksheetForm(forms.Form):
    name = forms.CharField(max_length=100, label="Student Name")
    roll_no = forms.IntegerField(label="Roll Number")
    subject1 = forms.IntegerField(label="Subject 1 Marks")
    subject2 = forms.IntegerField(label="Subject 2 Marks")
    subject3 = forms.IntegerField(label="Subject 3 Marks")
    subject4 = forms.IntegerField(label="Subject 4 Marks")
    subject5 = forms.IntegerField(label="Subject 5 Marks")
