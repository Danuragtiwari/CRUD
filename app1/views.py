from django.shortcuts import render,redirect 
from .forms import StudentForm
from .models import Student

# Create your views here.
def add(request):
    return render(request,'add.html')