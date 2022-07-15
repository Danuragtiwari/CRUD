from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

# Create your views here.
def  app(request):
    return HttpResponse("haa")
def index(request):
    # return HttpResponse("yeha tk thik h")
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
               form.save()
               return redirect('/home')
            except:
                pass

    form=StudentForm()
    return render(request,'hometohome.html',{'form':form}) #hometohome=index.html
def home(request):
    students=Student.objects.all()
    return render(request,'hometoshow.html',{'students':students})
    # return render(request,'add.html')