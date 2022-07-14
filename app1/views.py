from django.shortcuts import render,redirect 
from .forms import StudentForm
from .models import Student

# Create your views here.
def add(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
    if form.is_valid():
        form.save()
        

    return render(request,'add.html')