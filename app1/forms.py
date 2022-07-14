from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meat:
        model=Student 
        field='__all__'