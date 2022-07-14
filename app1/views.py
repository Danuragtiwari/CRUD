from django.shortcuts import render,redirect 
from .forms import StudentForm
from .models import Student

# Create your views here.
def add(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
               form.save()
               return redirect('/home')
            except:
                pass

    else:
        form=StudentForm()
    return render(request,'hometohome.html',{'form':form})
def home(request):
    students=Student.objects.all()
    return render(request,'hometoshow.html',{'students':students})
    # return render(request,'add.html')