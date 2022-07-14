# from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',add,name='add'),
    path('/home',home,name='home')
    # path('/home',home)
]
