# from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',app,name='app'),
    path('index/',index,name='index'),#index=emp
    path('home/',home,name='home')#home=show
    # path('/add',update,name='update')
    # path('/home',home)
]
